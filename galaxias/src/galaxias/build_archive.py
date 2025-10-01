import os
import pandas as pd
import zipfile
import corella
import delma
from .check_schema import check_schema
from .common_functions import add_file_to_dwca
from .use_data import use_data
from .use_schema import use_schema

def build_archive(occurrences=None,
                  events=None,
                  occurrences_filename='occurrences.csv',
                  events_filename='events.csv',
                  publishing_dir='./data-publish/',
                  metadata='eml.xml',
                  schema='meta.xml',
                  archive_name='dwca.zip',
                  print_report=False):
    """
    Checks all your files for Darwin Core compliance, and then creates the 
    Darwin Core archive in your working directory.

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
        ``archive_name``: ``str``
            Name of the Darwin Core Archive file you will create.  Default value is ``'dwca.zip'``.
        ``print_report``: ``str``
            Print your data report to screen.  Default value is ``'False'``.

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns ``None`` if it passes.
    """
    # check if occurrence data is in archive
    if isinstance(occurrences, pd.DataFrame):
        use_data(occurrences=occurrences,occurrences_filename=occurrences_filename)

    # check if event data is in archive
    if isinstance(events, pd.DataFrame):
        use_data(events=events,events_filename=events_filename)

    if occurrences is None:
        occurrences=pd.read_csv('{}/{}'.format(publishing_dir,occurrences_filename))
        if 'eventDate' in occurrences.columns:
            occurrences['eventDate'] = pd.to_datetime(occurrences['eventDate'])

    if events is None and os.path.exists('{}/{}'.format(publishing_dir,events_filename)):
        events=pd.read_csv('{}/{}'.format(publishing_dir,events_filename))
        if 'eventDate' in events.columns:
            events['eventDate'] = pd.to_datetime(events['eventDate'])

    # run basic checks on data
    data_check = corella.check_dataset(occurrences=occurrences,
                                       events=events,
                                       occurrences_filename=occurrences_filename,
                                       events_filename=events_filename,
                                       print_report=print_report)

    # run eml.xml check
    if not os.path.exists('{}/{}'.format(publishing_dir,metadata)):
        raise ValueError("Please create your metadata xml file (use_metadata function)")
    eml_xml_check = delma.check_metadata(eml_dir=publishing_dir,eml_xml=metadata)
    
    # run meta.xml check
    if not os.path.exists('{}/{}'.format(publishing_dir,schema)):
        use_schema()
    meta_xml_check = check_schema(schema=schema,publishing_dir=publishing_dir)
    
    # set the boolean for xml_check
    if eml_xml_check is None and meta_xml_check:
        xml_check = True
    else:
        xml_check = False

    print(data_check)
    print(eml_xml_check)
    print(meta_xml_check)

    # write dwca if data and xml passes
    if data_check and xml_check:
        
        # open archive
        zf = zipfile.ZipFile(archive_name,'w')

        # list for looping
        objects_list = [occurrences,events] # multimedia, emof
        filename_list = [occurrences_filename,events_filename] # ,multimedia_filename,emof_filename

        # looping over associated objects and filenames
        # for i,(dataframe,filename) in enumerate(zip(objects_list,filename_list)):
        for i,(dataframe,filename) in enumerate(zip(objects_list,filename_list)):
            if dataframe is not None:
                add_file_to_dwca(zf=zf,
                                 dataframe=dataframe,
                                 publishing_dir=publishing_dir,
                                 file_to_write=filename)
            elif os.path.isfile('{}/{}'.format(publishing_dir,filename)):
                zf.write("{}/{}".format(publishing_dir,filename))

        # write eml.xml
        zf.write("{}/{}".format(publishing_dir,metadata))
        
        # write meta.xml
        zf.write("{}/{}".format(publishing_dir,schema))
        
        # close zipfile
        zf.close()

    elif xml_check and not data_check and not print_report:
        raise ValueError("Please run check_dataset with the print_report option set to True to see what data needs to be checked.")
    elif xml_check and not data_check and print_report:
        raise ValueError("Please fix the flagged errors in your data.")
    else:
        if eml_xml_check is not None:
            raise ValueError("Your {} file is not formatted correctly.  Please run check_metadata() to see where the issue is.".format(metadata))
        if not meta_xml_check:
            raise ValueError("Your {} file is not formatted correctly.  Please run check_schema() to see where the issue is.".format(schema))