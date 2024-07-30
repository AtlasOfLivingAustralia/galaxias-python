import pandas as pd
import os
import zipfile
import shutil
from .common_dictionaries import TAXON_TERMS,TITLE_LEVELS,required_columns_event
from .get_dwc_noncompliant_terms import get_dwc_noncompliant_terms
from .read_dwc_terms_links import read_dwc_terms_links
from .build_subelement import build_subelement
from .check_data_functions import *
from .add_unique_occurrence_ids import add_unique_occurrence_IDs
# from dwca.read import DwCAReader
import xml.etree.ElementTree as ET
from operator import itemgetter
import subprocess
from tabulate import tabulate
from .print_dwca_report import print_dwca_report
import datetime

# TRYING THIS
import metapype
import metapype.eml.export
from metapype.eml.exceptions import MetapypeRuleError
import metapype.eml.names as names
import metapype.eml.validate as validate
from metapype.model.node import Node

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

        # create metadata file
        if not os.path.exists(self.metadata_md):
            self.create_metadata_file()
        
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
        Checks whether or not your data (occurrences) meets the pre-defined standard.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """

        # set up dict for dataframe
        required_terms = {
            "Type": ["Identifier (at least one)",
                     "Record type",
                     "Scientific name",
                     "Location",
                     "Date/Time"],
            "Matched term(s)": ['-','-','-','-','-'],
            "Missing term(s)": ['occurrenceID OR catalogNumber OR recordNumber',
                                'basisOfRecord',
                                'scientificName',
                                GEO_REQUIRED_DWCA_TERMS["Australia"],
                                'eventDate']
        }

        # get matching and nonmatching terms
        unmatched_dwc_terms = get_dwc_noncompliant_terms(self.occurrences)
        matched_dwc_terms = list(filter(lambda x: x not in unmatched_dwc_terms, list(self.occurrences.columns)))

        # list of all required terms
        terms = [
            ['occurrenceID', 'catalogNumber','recordNumber'],
            'basisOfRecord',
            'scientificName',
            GEO_REQUIRED_DWCA_TERMS["Australia"],
            'eventDate'
        ]

        # loop over all terms to compile what the person has int he dwca
        for i,t in enumerate(terms):
            if type(t) is list:
                if 'occurrenceID' in t:
                    # check for identifier
                    if any(map(lambda v: v in ['occurrenceID', 'catalogNumber','recordNumber'],list(self.occurrences.columns))):
                        column_present = list(map(lambda v: v in ['occurrenceID', 'catalogNumber','recordNumber'],list(self.occurrences.columns)))
                        true_indices = column_present.index(True)
                        if type(true_indices) is list:
                            required_terms["Matched term(s)"][0] = ', '.join(list(self.occurrences.columns)[true_indices])
                        else:
                            required_terms["Matched term(s)"][0] = list(self.occurrences.columns)[true_indices]
                        required_terms["Missing term(s)"][0] = '-'
                elif 'decimalLatitude' in t:
                    # check for Location
                    location_names = []
                    for name in GEO_REQUIRED_DWCA_TERMS["Australia"]:
                        if name in self.occurrences.columns:
                            location_names.append(name)
                            required_terms["Missing term(s)"][3].remove(name)
                    if len(location_names) == 0:
                        location_names = ['-']
                    if len(required_terms["Missing term(s)"][3]) == 0:
                        required_terms["Missing term(s)"][3] = ['-']
                    required_terms["Matched term(s)"][3] = ', '.join(location_names)
                    required_terms["Missing term(s)"][3] = ', '.join(required_terms["Missing term(s)"][3])
                else:
                    if t in list(self.occurrences.columns):
                        required_terms["Matched term(s)"][i] = t
                        required_terms["Missing term(s)"][i] = '-'

        # first, check if all required terms are there
        if required_terms["Missing term(s)"] == ['-','-','-','-','-']:
            
            # run data check
            errors = check_all_data(dataframe=self.occurrences)

            # check for errors in the data and change the dict accordingly
            messages = errors["errors"]

            # check for data errors
            if any(m != '-' for m in messages):

                # print data errors
                errors_df = pd.DataFrame(errors)
                print(tabulate(errors_df, showindex=False, headers=errors_df.columns))
                print("\nError: Invalid data detected in {} column(s).".format(list(m != '-' for m in messages).count(True)))
                print("\nSuggested workflow:\n")
                if any(map(lambda v: v in errors["Column"], ['occurrenceID','basisOfRecord'])):
                    for term in ['occurrenceID','basisOfRecord']:
                        if term in errors["Column"]:
                            index = errors["Column"].index(term)
                            if errors["errors"][index] != '-':
                                print("df.use_occurrences()")
                if any(map(lambda v: v in errors["Column"], ['scientificName'])):
                    index = errors["Column"].index('scientificName')
                    if errors["errors"][index] != '-':
                        print("df.use_scientific_name()")
                if any(map(lambda v: v in errors["Column"], GEO_REQUIRED_DWCA_TERMS["Australia"])):
                    for term in GEO_REQUIRED_DWCA_TERMS["Australia"]:
                        if term in errors["Column"]:
                            index = errors["Column"].index(term)
                            if errors["errors"][index] != '-':
                                print("df.use_coordinates()")
                if any(map(lambda v: v in errors["Column"], ['eventDate', 'day', 'month', 'year', 'time'])):
                    for term in ['eventDate', 'day', 'month', 'year', 'time']:
                        if term in errors["Column"]:
                            index = errors["Column"].index(term)
                            if errors["errors"][index] != '-':
                                print("df.use_datetime()")    

            else:

                print_dwca_report(dataframe=self.occurrences,
                              matched_dwc_terms=matched_dwc_terms,
                              unmatched_dwc_terms=unmatched_dwc_terms,
                              required_terms=required_terms)

        else:

            print_dwca_report(dataframe=self.occurrences,
                              matched_dwc_terms=matched_dwc_terms,
                              unmatched_dwc_terms=unmatched_dwc_terms,
                              required_terms=required_terms)

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

        # # first, check for events
        # if self.events is not None:

        #     # events_pass = self.check_events()
        #     occurrences_pass = self.check_data()
        #     print("need to write this")

            # if self.multimedia is not None:
            #     multimedia_pass = self.check_multimedia()
            #     if not multimedia_pass:
            #         raise ValueError("You need to check your multimedia files to make sure they are DwC compliant.")

            # if self.emof is not None:
            #     emof_pass = self.check_emof()
            #     if not emof_pass:
            #         raise ValueError("You need to check your multimedia files to make sure they are DwC compliant.")
                
            # if events_pass and occurrences_pass:
            #     if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)) and os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
            #         return True
            #     else:
            #         raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')
            # elif not events_pass:
            #     raise ValueError("You need to check your events to make sure they are DwC compliant.")
            # elif not occurrences_pass:
            #     raise ValueError("You need to check your occurrences to make sure they are DwC compliant.")
            # else:
            #     raise ValueError("You need to check your events and occurrences to make sure they are DwC compliant.")
        
        # next, check for occurrences
        if self.occurrences is not None:
            
            occurrences_pass = self.check_data()

            # if self.multimedia is not None:
            #     multimedia_pass = self.check_multimedia()
            #     if not multimedia_pass:
            #         raise ValueError("You need to check your multimedia files to make sure they are DwC compliant.")

            if occurrences_pass:
                if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)) and os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
                    return True
                else:
                    raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')
            else:
                raise ValueError('Your occurrences are not formatted correctly.')

        else:
            return False
    
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

        # run xml check
        xml_check = check_xmls()
        if xml_check is None:
            xml_check = True

        # data_check = xml_check = True
        
        if data_check and xml_check:
            
            # zip everything into file
            if self.events is not None:
                
                # open archive
                zf = zipfile.ZipFile(self.dwca_name,'w')

                # check if your data file has been written
                if not os.path.exists("{}/{}".format(self.data_proc_dir,self.occurrences_dwc_filename)):
                    self.occurrences.to_csv("{}/{}".format(self.data_proc_dir,self.occurrences_dwc_filename),index=False)

                # first, write occurrences to zip and disk
                os.system("cp {}/{} .".format(self.data_proc_dir,self.occurrences_dwc_filename))
                zf.write(self.occurrences_dwc_filename)
                os.system("rm {}".format(self.occurrences_dwc_filename))

                # check if your data file has been written
                if not os.path.exists("{}/{}".format(self.data_proc_dir,self.events_dwc_filename)):
                    self.events.to_csv("{}/{}".format(self.data_proc_dir,self.events_dwc_filename),index=False)

                # then, write events
                os.system("cp {}/{} .".format(self.data_proc_dir,self.events_dwc_filename))
                zf.write(self.events_dwc_filename)
                os.system("rm {}".format(self.events_dwc_filename))

                # then, write multimedia if it exists
                if self.multimedia is not None:

                    # check if data exists on disk
                    if not os.path.exists("{}/{}".format(self.data_proc_dir,self.multimedia_dwc_filename)):
                        self.multimedia.to_csv("{}/{}".format(self.data_proc_dir,self.multimedia_dwc_filename),index=False)
                    
                    # write to dwca
                    os.system("cp {}/{} .".format(self.data_proc_dir,self.multimedia_dwc_filename))
                    zf.write(self.multimedia_dwc_filename)
                    os.system("rm {}".format(self.multimedia_dwc_filename))

                # then, write multimedia if it exists
                if self.emof is not None:
                    
                    # check if data exists on disk
                    if not os.path.exists("{}/{}".format(self.data_proc_dir,self.emof_dwc_filename)):
                        self.emof.to_csv("{}/{}".format(self.data_proc_dir,self.emof_dwc_filename),index=False)
                    
                    # write to dwca
                    os.system("cp {}/{} .".format(self.data_proc_dir,self.emof_dwc_filename))
                    zf.write(self.emof_dwc_filename)
                    os.system("rm {}".format(self.emof_dwc_filename))

            else:

                # open archive
                zf = zipfile.ZipFile(self.dwca_name,'w')

                # check if your data file has been written
                if not os.path.exists("{}/{}".format(self.data_proc_dir,self.occurrences_dwc_filename)):
                    self.occurrences.to_csv("{}/{}".format(self.data_proc_dir,self.occurrences_dwc_filename),index=False)

                # first, write occurrences
                os.system("cp {}/{} .".format(self.data_proc_dir,self.occurrences_dwc_filename))
                zf.write(self.occurrences_dwc_filename)
                os.system("rm {}".format(self.occurrences_dwc_filename))

                # then, write multimedia if it exists
                if self.multimedia is not None:
                    if not os.path.exists("{}/{}".format(self.data_proc_dir,self.multimedia_dwc_filename)):
                        self.multimedia.to_csv("{}/{}".format(self.data_proc_dir,self.multimedia_dwc_filename),index=False)
                    
                    # write to dwca
                    os.system("cp {}/{} .".format(self.data_proc_dir,self.multimedia_dwc_filename))
                    zf.write(self.multimedia_dwc_filename)
                    os.system("rm {}".format(self.multimedia_dwc_filename))

            # ensure metadata files are there
            if os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
                os.system("cp {}/{} .".format(self.working_dir,self.eml_xml))
                zf.write(self.eml_xml)
                os.system("rm {}".format(self.eml_xml))
            else:
                raise ValueError("You need to create your metadata files (eml.xml and meta.xml) - use the function make_meta_xml().")    

            if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)):
                os.system("cp {}/{} .".format(self.working_dir,self.meta_xml))
                zf.write(self.meta_xml)
                os.system("rm {}".format(self.meta_xml))
            else:
                raise ValueError("You need to create your metadata files (eml.xml and meta.xml) - use the function make_meta_xml().")         
           
            # close zipfile
            zf.close()

        elif not data_check and xml_check:
            raise ValueError("Your data did not pass our basic compliance checks.")
        elif data_check and not xml_check:
            raise ValueError("Your xmls did not pass our basic compliance checks.")
        else:
            raise ValueError("Neither your data nor your xmls passed our compliance checks")

    def create_metadata_file(self):
        """
        Creates a markdown file containing the metadata information needed for the DwCA.  The user can edit this 
        markdown, and use it to generate the metadata files.

        Parameters
        ----------
            ``filename`` : ``str``
                Option whether to return a dictionary object containing full taxonomic information on your species.  Default to ``False``. 
            ``path`` : ``str``
                File path to your working directory.  Default is directory you are currently in.

        Returns
        -------
            ``None``
        """
        
        if not os.path.exists(self.metadata_md):
            os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),os.path.join(self.metadata_md)))
        else:
            pass
    
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

        ## TODO: ADD THIS BACK IN
        # if len(list(set(list(self.occurrences.columns)).intersection(list(dwc_terms_info['name'])))) < self.occurrences.shape[1]:
        #     raise ValueError("You are still missing some DwCA Terms.")

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
        
    def make_eml_xml(self):
        """
        Makes the ``eml.xml`` file from the metadata markdown file into your current working directory.  
        The ``eml.xml`` file is the metadata file containing things like authorship, licence, institution, 
        etc.

        Parameters
        ----------
            ``None``
                    
        Returns
        -------
            ``None``
        """
       
        # initialise the eml.xml file
        metadata = Node(names.EML)
        metadata.add_attribute('packageId', 'edi.23.1') # doi:10.xxxx/eml.1.1
        metadata.add_attribute('system', 'ALA-registry')

        # initialise elements
        elements = {}
        titles = {}
        level_dict = {0: metadata,
                      1 : None,
                      2 : None,
                      3 : None,
                      4 : None,
                      5 : None,
                      6 : None}

        # check for last line
        import subprocess
        last_line = subprocess.check_output(['tail', '-1', self.metadata_md],text=True).strip()

        # open the metadata file
        metadata_file = open(self.metadata_md, "r")

        # initialise list so we have everything in order
        title_list = []

        # loop over things in metadata
        title = ""
        description = ""
        duplicate = 0
        for line in metadata_file:
            if line != "\n":
                if "#" == line[0]:
                    title_parts = line.strip().split(' ')
                    title = "".join(title_parts[1:]).upper()
                    titles[title] = TITLE_LEVELS[title_parts[0]]
                    title_list.append(title)
                    if line.strip() == last_line:
                        elements[title] = ''
                else:
                    if description != "":
                        description.append(line.strip())
                    else:
                        description = [line.strip()]
                    if line.strip() == last_line:
                        elements[title] = description
            elif line == "\n" and title != "" and description != "":
                if title not in elements:
                    elements[title] = description
                else:
                    elements["{}{}".format(title,duplicate)] = description
                    duplicate += 1
                title = ""
                description = ""
            elif line == "\n" and title != "":
                if title not in elements:
                    elements[title] = ""
                else:
                    elements["{}{}".format(title,duplicate)] = ""
                    duplicate += 1
                title = ""
            else:
                pass

        # close markdown file
        metadata_file.close()

        # loop over all levels
        for t in title_list:
            
            # check for duplicates
            if t[-1].isdigit():
                t = t[:-1]
            elif t[-2:].isdigit():
                t = t[:-2]

            # get attribute and set nodes
            attr = getattr(names,t)
            current_node = Node(attr,parent=level_dict[titles[t] - 1])
            if type(elements[t]) is list:
                current_node.content = "".join(elements[t])
            level_dict[titles[t]] = current_node
            level_dict[titles[t] - 1].add_child(current_node)
            
        # write xml
        xml_str = metapype.eml.export.to_xml(metadata)
        with open("{}/{}".format(self.working_dir,self.eml_xml), 'w') as f:
            f.write(xml_str)

    def use_coordinates(self,
                        decimalLatitude=None,
                        decimalLongitude=None,
                        geodeticDatum=None,
                        coordinateUncertaintyInMeters=None,
                        coordinatePrecision=None,
                        assign = True):
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            decimalLatitude: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents latitude (unit in degrees).
            decimalLongitude: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents longitude (unit in degrees).
            geodeticDatum: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the coordinate reference system (CRS).
            coordinateUncertaintyInMeters: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the uncertainty of the instrument measuring 
                the latitude and longitude (unit is meters).
            coordinatePrecision: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the inherent uncertainty of your measurement 
                (unit in degrees).

        Returns
        -------
            Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
        """

        # make copy of occurrences
        temp_occurrences = self.occurrences.copy()

        # mapping here for later
        mapping = {}

        if all(map(lambda v: v not in GEO_REQUIRED_DWCA_TERMS["Australia"],list(self.occurrences.columns))):
            raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(self.use_coordinates()) for valid arguments.")

        # check if each variable is None
        if decimalLatitude is not None:
            mapping[decimalLatitude.name] = 'decimalLatitude'

        if decimalLongitude is not None:
            mapping[decimalLongitude.name] = 'decimalLongitude'

        if geodeticDatum is not None:
            if type(geodeticDatum) is pd.core.series.Series:
                mapping[geodeticDatum.name] = 'geodeticDatum'
            elif type(geodeticDatum) is str:
                temp_occurrences['geodeticDatum'] = geodeticDatum
            else:
                raise ValueError("Only a string or pandas series is accepted for geodeticDatum")

        if coordinateUncertaintyInMeters is not None:
            if type(coordinateUncertaintyInMeters) is pd.core.series.Series:
                mapping[coordinateUncertaintyInMeters.name] = 'coordinateUncertaintyInMeters'
            elif (type(coordinateUncertaintyInMeters) is int or type(coordinateUncertaintyInMeters) is float):
                temp_occurrences['coordinateUncertaintyInMeters'] = coordinateUncertaintyInMeters
            else:
                raise ValueError("Only an int, float or pandas series is accepted for coordinateUncertaintyInMeters")

        if coordinatePrecision is not None:
            if type(coordinatePrecision) is pd.core.series.Series:
                mapping[coordinatePrecision.name] = 'coordinatePrecision'
            elif (type(coordinatePrecision) is int or type(coordinatePrecision) is float):
                temp_occurrences['coordinatePrecision'] = coordinatePrecision
            else:
                raise ValueError("Only an int, float or pandas series is accepted for coordinatePrecision")

        # rename all necessary columns
        temp_occurrences = temp_occurrences.rename(columns=mapping)

        # check all required variables
        check_coordinates(dataframe=temp_occurrences)

        # set new occurrences to object
        if assign:
            self.occurrences = temp_occurrences
        else:
            print(temp_occurrences)

    def use_datetime(self,
                     eventDate=None,
                     year=None,
                     month=None,
                     day=None,
                     time=None,
                     string_to_datetime=False,
                     orig_format='%d-%m-%Y'):
        """
        Checks for time information, such as the date an occurrence occurred.  Also runs checks 
        on the validity of the format of the date.

        Parameters
        ----------
            eventDate: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the date of the occurrences.
            year: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the year of the occurrence.
            month: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the date of the occurrences.
            day: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the day of the occurrences.
            time: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the time of the occurrences.
            string_to_datetime: ``logical``
                An argument that tells ``galaxias`` to convert dates that are in a string format 
                to a ``datetime`` format.  Default is ``False``.
            orig_format: ``str``
                A string denoting the original format of the dates that are being converted from a 
                string to a ``datetime`` object.  Default is ``'%d-%m-%Y'``.

        Returns
        -------
            Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
        """

        if all(map(lambda v: v not in ["eventDate","year","month","day", "time"],list(self.occurrences.columns))):
            raise ValueError("No Darwin Core arguments supplied to `use_datetime()`.  See dir(self.use_datetime()) for valid arguments.")

        # create a temporary occurrences variable
        temp_occurrences = self.occurrences

        # create a dictionary of names for renaming
        names = {}

        for var in [eventDate,year,month,day,time]:
            if var is not None and var is eventDate:
                names[var.name] = 'eventDate'
            elif var is not None and var is year:
                names[var.name] = 'year'
            elif var is not None and var is month:
                names[var.name] = 'month'
            elif var is not None and var is day:
                names[var.name] = 'day'
            elif var is not None and var is time:
                names[var.name] = 'time'
            else:
                pass

        # check name of columns
        for var in [eventDate,year,month,day,time]:
            if var is not None:        
                if type(var) is datetime.datetime:
                    pass
                elif type(var) is pd.core.series.Series:
                    temp_occurrences = temp_occurrences.rename(columns={var.name: names[var.name]})
                else:
                    raise ValueError("only accepts datetime data types or pandas series as eventDate")

        # options to convert strings to datetime
        if string_to_datetime:
            for i,entry in enumerate(temp_occurrences['eventDate']):
                temp_occurrences['eventDate'][i] = datetime.datetime.strptime(entry,orig_format)

        # check format
        check_eventDate(dataframe=temp_occurrences)
        
        # assign updated occurrences to object
        self.occurrences = temp_occurrences

    def use_locality(self,
                     continent = None,
                     country = None,
                     countryCode = None,
                     stateProvince = None,
                     locality = None):
        """
        (OPTIONAL) Checks for additional location information, such as country and countryCode.

        Parameters
        ----------
            continent: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the continent of the occurrences.
            country: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the country of the occurrence.
            countryCode: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the countryCode of the occurrences.
            stateProvince: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the stateProvince of the occurrences.
            locality: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the locality of the occurrences.
        Returns
        -------
            Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
        """

        if all(map(lambda v: v not in ["continent","country","countryCode","stateProvince", "locality"],list(self.occurrences.columns))):
            raise ValueError("No Darwin Core arguments supplied to `use_locality()`.  See dir(self.use_locality()) for valid arguments.")
        
        # create a temporary occurrences variable
        temp_occurrences = self.occurrences

        # create a dictionary of names for renaming
        names = {}

        for var in [continent,country,countryCode,stateProvince,locality]:
            if var is not None and var is continent:
                names[var.name] = 'continent'
            elif var is not None and var is country:
                names[var.name] = 'country'
            elif var is not None and var is countryCode:
                names[var.name] = 'countryCode'
            elif var is not None and var is stateProvince:
                names[var.name] = 'stateProvince'
            elif var is not None and var is locality:
                names[var.name] = 'locality'
            else:
                pass

        # check name of columns
        for var in [continent,country,countryCode,stateProvince,locality]:
            if var is not None:        
                if type(var) is str:
                    pass
                elif type(var) is pd.core.series.Series:
                    temp_occurrences = temp_occurrences.rename(columns={var.name: names[var.name]})
                else:
                    raise ValueError("only accepts str types or pandas series as {}".format(var.name))
        
        check_locality(dataframe=temp_occurrences)

        self.occurrences = temp_occurrences


    def use_occurrences(self,occurrenceID=None,basisOfRecord=None):
        """
        Checks for unique identifiers of each occurrence and how the occurrence was recorded.

        Parameters
        ----------
            occurrenceID: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the unique occurrenceIDs of the occurrences.
            basisOfRecord: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents how the occurrence was recorded.

        Returns
        -------
            Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
        """

        if occurrenceID is not None or basisOfRecord is not None:

            # create temporary occurrences
            temp_occurrences = self.occurrences.copy()

            if occurrenceID is not None:
                if type(occurrenceID) is bool:
                    temp_occurrences = add_unique_occurrence_IDs(column_name='occurrenceID',
                                                                 dataframe=temp_occurrences)
                elif type(occurrenceID) is pd.core.series.Series:
                    temp_occurrences['occurrenceID'] = occurrenceID.copy()
                    temp_occurrences.drop(occurrenceID.name,axis=1)
                else:
                    raise ValueError("occurrenceID argument must be a boolean or pandas Series (i.e. column)")

                # check values
                check_occurrenceIDs(dataframe=temp_occurrences)

            if basisOfRecord is not None:
                if type(basisOfRecord) is str:
                    temp_occurrences['basisOfRecord'] = basisOfRecord
                elif type(basisOfRecord) is pd.core.series.Series:
                    temp_occurrences['basisOfRecord'] = basisOfRecord.copy()
                    temp_occurrences.drop(basisOfRecord.name,axis=1)
                else:
                    raise ValueError("occurrenceID argument must be a string or pandas Series (i.e. column)")

                # check values
                check_basisOfRecord(dataframe=temp_occurrences) 

        else:
            
            raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(self.use_occurrences()) for valid arguments.")
           

        # assign new occurrences to archive
        self.occurrences = temp_occurrences

    def use_scientific_name(self,scientific_name=None):
        """
        Checks for the name of the taxon you identified is present.

        Parameters
        ----------
            scientific_name: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the taxonomic identification of the occurrences.

        Returns
        -------
            Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
        """

        if scientific_name is not None:

            # create temporary occurrences
            temp_occurrences = self.occurrences.copy()

            # check type of variable
            if type(scientific_name) is pd.core.series.Series:
                temp_occurrences['scientificName'] = scientific_name.copy()
                temp_occurrences = temp_occurrences.drop(scientific_name.name,axis=1)
            else:
                raise ValueError("occurrenceID argument must be a pandas Series (i.e. column)")

            # check values
            check_scientificName(dataframe=temp_occurrences)

            # assign temp_occurrences to occurrences
            self.occurrences = temp_occurrences
        
        else:

            raise ValueError("No Darwin Core arguments supplied to `use_scientific_name()`.  See dir(self.use_scientific_name()) for valid arguments.")