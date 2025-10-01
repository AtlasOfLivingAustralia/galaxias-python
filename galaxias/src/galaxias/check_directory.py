import os
import zipfile
import pandas as pd
import corella
from .check_metadata import check_metadata
from .check_schema import check_schema

def check_directory(archive_name = 'dwca.zip',
                    occurrences_filename='occurrences.csv',
                    events_filename='events.csv',
                    metadata='eml.xml',
                    schema='meta.xml',
                    publishing_dir='./data-publish/',
                    print_report=False):
    """
    Checks whether or not your Darwin Core Archive is formatted correctly.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.
    """
    # first, check all files exist in the Darwin Core Archive
    archive = zipfile.ZipFile(archive_name)
    names = archive.namelist()
    occ_filename = parse_name(name='{}/{}'.format(publishing_dir,occurrences_filename))
    metadata_filename = parse_name(name='{}/{}'.format(publishing_dir,metadata))
    schema_filename = parse_name(name='{}/{}'.format(publishing_dir,schema))
    
    # check for occurrences
    if occ_filename not in names:
        raise ValueError('You need to have an occurrences file in your archive.')
    
    if metadata_filename not in names:
        raise ValueError('You need to have a metadata file in your archive.')
    
    if schema_filename not in names:
        raise ValueError('You need to have a schema file in your archive.')

    result = corella.check_dataset(occurrences=None,
                                   events=None,
                                   # multimedia=multimedia,
                                   # emof=emof,
                                   occurrences_filename=occurrences_filename,
                                   events_filename=events_filename,
                                   publishing_dir=publishing_dir,
                                   print_report=print_report)
    # check the metadata
    if result:

        if os.path.exists(metadata_filename) and os.path.exists(schema_filename):
            check_metadata(eml_dir=publishing_dir,eml_xml=metadata)
            check_schema(schema=schema,publishing_dir=publishing_dir)
            return True
        else:
            raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')

    else:
        raise ValueError("Some of your data does not comply with the Darwin Core standard.  Please run corella.check_data() and/or corella.suggest_workflow().")

def parse_name(name = None):
    if name[0:2] == './':
        name = name[2:]
    name = name.replace('//','/')
    return name