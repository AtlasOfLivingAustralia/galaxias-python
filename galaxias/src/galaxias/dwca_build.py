import pandas as pd
import os
import zipfile
import shutil
from .read_dwc_terms_links import read_dwc_terms_links
from .build_subelement import build_subelement
from .common_functions import add_file_to_dwca,write_to_zip_and_disk
# from dwca.read import DwCAReader
import xml.etree.ElementTree as ET
from operator import itemgetter
import subprocess
import corella
import paperbark

class dwca:

    def __init__(self,
                 working_dir = 'dwca_data',
                 data_raw_dir = 'data_raw',
                 data_proc_dir = 'data_processed',
                 dwca_name = 'dwca.zip',
                 occurrences = None,
                 occurrences_dwc_filename = 'occurrences.txt',
                 multimedia = None,
                 multimedia_dwc_filename = 'multimedia.txt',
                 events = None,
                 events_dwc_filename = 'events.txt',
                 emof = None,
                 emof_dwc_filename = 'extendedMeasurementOrFact.txt', # was .csv
                 metadata_md = 'metadata.md',
                 eml_xml = 'eml.xml',
                 meta_xml = 'meta.xml'
                 ):

        # initialise variables
        current_dir = subprocess.check_output("pwd",shell=True,text=True).strip()
        self.working_dir = '{}/{}'.format(current_dir,working_dir)
        self.data_raw_dir = '{}/{}/{}'.format(current_dir,working_dir,data_raw_dir)
        self.data_proc_dir = '{}/{}/{}'.format(current_dir,working_dir,data_proc_dir)
        self.dwca_name = '{}/{}/{}'.format(current_dir,working_dir,dwca_name)
        self.occurrences = occurrences
        self.occurrences_dwc_filename = occurrences_dwc_filename
        self.multimedia = multimedia
        self.multimedia_dwc_filename = multimedia_dwc_filename
        self.events = events
        self.events_dwc_filename = events_dwc_filename
        self.emof = emof
        self.metadata_md = '{}/{}/{}'.format(current_dir,working_dir,metadata_md)
        self.emof_dwc_filename = emof_dwc_filename
        self.eml_xml = eml_xml
        self.meta_xml = meta_xml

        # make the working directory
        folders =  ['working_dir','data_raw_dir','data_proc_dir']
        for folder in folders:
            folder_name = getattr(self,folder)
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
        
        # now initialise the data variables
        vars = ['occurrences','multimedia','events','emof']

        # loop over all data variables
        for var in vars:

            # get value of variable
            var_value = getattr(self,var)

            # check for valid value of data variable
            if var_value is None or type(var_value) is pd.core.frame.DataFrame:
                # object, attribute, value
                setattr(self,var,var_value) 
                if var == 'occurrences' and var_value is None:
                    print('WARNING: You will need occurrences for both Darwin Core and Event Core Archives.')
            elif type(var_value) is str:
                if 'csv' in var_value:
                    shutil.copy2(var_value,self.data_raw_dir)
                    setattr(self,var,pd.read_csv(var_value))
                else:
                    raise ValueError("If providing a filename, you must provide a csv file")
            else:
                raise ValueError("Only a csv filename or Pandas dataframe will be accepted for {}.".format(var))

    def check_data(self):
        """
        Checks whether or not your data (only occurrences for now) meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        result = corella.check_data(occurrences=self.occurrences,
                                    events=self.events,
                                    # multimedia=self.multimedia,
                                    # emof=self.emof,
                                    print_report=False)
        if result:
            return result
        print("Your data does not comply with the Darwin Core standard.  Please run corella.check_data() and/or corella.suggest_workflow().")

    def check_dwca(self):
        """
        Checks whether or not your Darwin Core Archive meets the pre-defined standard.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is wrong, or returns True if it passes.
        """

        # get all variables
        vars_dict = vars(self)
        self_vars = list(vars(self).keys())
        data_vars = [x for x in self_vars if 'xml' not in x and 'name' not in x and 'md' not in x]
        
        # determine what type of archive it is
        data_files = list(itemgetter(*data_vars)(vars_dict))
        
        # check for empty archive
        if all(type(x) == type(data_files[0]) for x in data_files):
            raise ValueError("You have no data in your DwCA.  Please at least add occurrences")
        
        result = corella.check_data(occurrences=self.occurrences,
                                    events=self.events,
                                    # multimedia=self.multimedia,
                                    # emof=self.emof,
                                    print=False)
        if result:

            if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)) and os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
                return True
            else:
                raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')

        else:
            raise ValueError("Some of your data does not comply with the Darwin Core standard.  Please run corella.check_data() and/or corella.suggest_workflow().")
    
    def check_eml_xml(self):
        """
        Checks whether or not your data (only occurrences for now) meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        if os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
            paperbark.check_eml_xml(eml_xml=self.eml_xml)
        else:
            raise ValueError()
        
    def check_meta_xml(self):
        """
        Checks whether or not your data (only occurrences for now) meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)):
            return True
        else:
            raise ValueError()

    def create_dwca(self):
        """
        Checks all your files for Darwin Core compliance, and then creates the 
        Darwin Core archive in your working directory.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is wrong, or returns ``None`` if it passes.
        """
        # run basic checks on data
        data_check = self.check_dwca()

        # run eml.xml check
        eml_xml_check = self.check_eml_xml()

        # run meta.xml check
        meta_xml_check = self.check_meta_xml()

        # set the boolean for xml_check
        if xml_check is None:
            xml_check = True

        # write dwca if data and xml passes
        if data_check and eml_xml_check and meta_xml_check:
            
            # open archive
            zf = zipfile.ZipFile(self.dwca_name,'w')

            # list for looping
            objects_list = [self.occurrences,self.events,self.multimedia,self.emof]
            filename_list = [self.occurrences_dwc_filename,self.events_dwc_filename,self.multimedia_dwc_filename,self.emof_dwc_filename]

            # looping over associated objects and filenames
            for dataframe,filename in enumerate(zip(objects_list,filename_list)):
                print("testing...")
                print(dataframe)
                print(filename)
                import sys
                sys.exit()
                if dataframe is not None:
                    add_file_to_dwca(zf=zf,
                                    dataframe=dataframe,
                                    file_to_write='{}/{}'.format(self.data_proc_dir,filename),
                                    removefile=filename)

            # write eml.xml
            write_to_zip_and_disk(zf=zf,
                                      copyfile="{}/{} .".format(self.working_dir,self.eml_xml),
                                      removefile=self.eml_xml)  
              
            # write meta.xml
            write_to_zip_and_disk(zf=zf,
                        copyfile="{}/{} .".format(self.working_dir,self.meta_xml),
                        removefile=self.meta_xml)
            
            # close zipfile
            zf.close()
    
    def make_meta_xml(self):
        """
        Makes the ``metadata.xml`` file from your ``eml.xml`` file and information from your ``occurrences`` 
        / other included extensions.  The ``metadata.xml`` file is your descriptor file, in that it describes 
        what is in the DwCA.

        Parameters
        ----------
            ``None``

        Returns
        -------
            ``None``
        """

        # check for at least occurrences
        if self.occurrences is None:
            raise ValueError("You need to have a passing, valid occurrence dataframe for this")
        
        # get list
        mylist = sorted(list(self.occurrences.columns),
                    key=lambda x: x == 'occurrenceID',
                    reverse=True)
        self.occurrences = self.occurrences[mylist]

        # get dwc terms
        dwc_terms_info = read_dwc_terms_links()

        # initialise metadata
        metadata = ET.Element("archive")
        metadata.set('xmlns', 'http://rs.tdwg.org/dwc/text/')
        metadata.set('metadata',self.eml_xml)

        # set the core of the archive and for
        core = ET.SubElement(metadata,"core")

        # check if it is an eventCore or an occurrenceCore
        if self.events is not None:
            core = build_subelement(element=core,
                                    row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                    filename=self.occurrences_dwc_filename,
                                    data=self.occurrences,
                                    dwc_terms_info=dwc_terms_info)
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/Event',
                                    filename=self.events_dwc_filename,
                                    data=self.events,
                                    dwc_terms_info=dwc_terms_info)
        else:
            core = build_subelement(element=core,
                                    row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                    filename=self.occurrences_dwc_filename,
                                    data=self.occurrences,
                                    dwc_terms_info=dwc_terms_info)

        # Extensions
        if self.multimedia is not None:
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/Multimedia',
                                    filename=self.multimedia_dwc_filename,
                                    data=self.multimedia,
                                    dwc_terms_info=dwc_terms_info)

        if self.emof is not None:
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/MeasurementOrFact',
                                    filename=self.emof_dwc_filename,
                                    data=self.emof,
                                    dwc_terms_info=dwc_terms_info)

        # write metadata
        tree = ET.ElementTree(metadata)
        ET.indent(tree, space="\t", level=0)
        tree.write("{}/{}".format(self.working_dir,self.meta_xml), xml_declaration=True)