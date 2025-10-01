import os
import pandas as pd
import xml.etree.ElementTree as ET
from .common_functions import read_dwc_terms_links,build_subelement

def use_schema(occurrences=None,
               events=None,
               occurrences_filename='occurrences.csv',
               events_filename='events.csv',
               publishing_dir='./data-publish/',
               metadata='eml.xml',
               schema='meta.xml'):
    """
    Makes the schema (``metadata.xml``) file from your  metadata (``eml.xml``) file and information from your 
    ``occurrences`` / ``events``.  

    Parameters
    ----------
        ``occurrences``: ``pandas DataFrame`` 
            OPTIONAL: This is the dataframe holding your occurrence data.  Default is ``None``.
        ``events``: ``pandas DataFrame`` 
            OPTIONAL: This is the dataframe holding your occurrence data.  Default is ``None``.
        ``occurrences_filename``: ``str``
            Name of your occurrences file.  Default value is ``'occurrences.csv'``.
        ``events_filename``: ``str``
            Name of your events file.  Default value is ``'events.csv'``.
        ``publishing_dir``: ``str``
            Name of the directory where all your processed data lives.  Default value is ``'./data-publish/'``.
        ``metadata``: ``str``
            Name of your metadata xml.  Default value is ``'eml.xml'``.
        ``schema``: ``str``
            Name of your schema xml.  Default value is ``'meta.xml'``.

    Returns
    -------
        ``None``
    """
    # check for at least occurrences
    if (occurrences is None) and (not os.path.exists('{}/{}'.format(publishing_dir,occurrences_filename))):
        raise ValueError("You need to provide either an occurrences dataframe or a valid occurrences filename to generate the schema.")
    
    # check to see if user has provided a file instead of a dataframe
    if (occurrences is None) and (os.path.exists('{}/{}'.format(publishing_dir,occurrences_filename))):
        occurrences = pd.read_csv('{}/{}'.format(publishing_dir,occurrences_filename))
    
    # check for events dataframe and/or whether the user has provided a filename instead
    if (events is None) and (os.path.exists('{}/{}'.format(publishing_dir,events_filename))):
        events = pd.read_csv('{}/{}'.format(publishing_dir,events_filename))

    # get list of columns sorted by event ID
    mylist = sorted(list(occurrences.columns),
                    key=lambda x: x == 'occurrenceID',
                    reverse=True)
    occurrences = occurrences[mylist]

    # get dwc terms
    dwc_terms_info = read_dwc_terms_links()

    # initialise metadata
    schema_data = ET.Element("archive")
    schema_data.set('xmlns', 'http://rs.tdwg.org/dwc/text/')
    schema_data.set('metadata',metadata)

    # set the core of the archive and for
    core = ET.SubElement(schema_data,"core")

    # check if it is an eventCore or an occurrenceCore
    if events is not None:
        core = build_subelement(element=core,
                                row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                filename=occurrences_filename,
                                data=occurrences,
                                dwc_terms_info=dwc_terms_info)
        ext = ET.SubElement(schema_data,"extension")
        ext = build_subelement(element=ext,
                                row_type='http://rs.tdwg.org/dwc/terms/Event',
                                filename=events_filename,
                                data=events,
                                dwc_terms_info=dwc_terms_info)
    else:
        core = build_subelement(element=core,
                                row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                filename=occurrences_filename,
                                data=occurrences,
                                dwc_terms_info=dwc_terms_info)

    # Extensions
    '''
    if multimedia is not None:
        ext = ET.SubElement(schema_data,"extension")
        ext = build_subelement(element=ext,
                                row_type='http://rs.tdwg.org/dwc/terms/Multimedia',
                                filename=multimedia_archive_filename,
                                data=multimedia,
                                dwc_terms_info=dwc_terms_info)

    if emof is not None:
        ext = ET.SubElement(schema_data,"extension")
        ext = build_subelement(element=ext,
                                row_type='http://rs.tdwg.org/dwc/terms/MeasurementOrFact',
                                filename=emof_archive_filename,
                                data=emof,
                                dwc_terms_info=dwc_terms_info)
    '''

    # write metadata
    tree = ET.ElementTree(schema_data)
    ET.indent(tree, space="\t", level=0)
    tree.write("{}/{}".format(publishing_dir,schema), xml_declaration=True)