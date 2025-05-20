import pandas as pd
import os
from .galaxias_config import readConfig
from .dwca_report import dwca_report
import json
import uuid
import requests
import zipfile
import shutil
import xmlschema
from .common_dictionaries import TAXON_TERMS,TITLE_LEVELS,required_columns_event
from .common_functions import get_dwc_noncompliant_terms,read_dwc_terms_links
# from dwc_validator.validate import validate_occurrence_dataframe,validate_media_extension
# from dwc_validator.validate import validate_event_dataframe,validate_emof_extension
import xml.etree.ElementTree as ET
from operator import itemgetter
import subprocess

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
                 occurrences_dwc_filename = 'occurrences.csv',
                 multimedia = None,
                 multimedia_dwc_filename = 'multimedia.csv',
                 events = None,
                 events_dwc_filename = 'events.csv',
                 emof = None,
                 emof_dwc_filename = 'extendedMeasurementOrFact.csv',
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
        self.occurrences_dwc_filename = '{}/{}'.format(self.data_proc_dir,occurrences_dwc_filename)
        self.multimedia = multimedia
        self.multimedia_dwc_filename = '{}/{}'.format(self.data_proc_dir,multimedia_dwc_filename)
        self.events = events
        self.events_dwc_filename = '{}/{}'.format(self.data_proc_dir,events_dwc_filename)
        self.emof = emof
        self.metadata_md = '{}/{}/{}'.format(current_dir,working_dir,metadata_md)
        self.emof_dwc_filename = '{}/{}'.format(self.data_proc_dir,emof_dwc_filename)
        self.eml_xml = '{}/{}/{}'.format(current_dir,working_dir,eml_xml)
        self.meta_xml = '{}/{}/{}'.format(current_dir,working_dir,meta_xml)

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

    def add_taxonomic_information(self):
        """
        Adds full taxonomic information (from kingdom to species) to your data for clearer identification

        Parameters
        ----------
            ``None``

        Returns
        -------
            ``None``

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc_rename.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.add_taxonomic_information()
            my_dwca.occurrences
            
        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc_rename.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_taxonomic_information();print(my_dwca.occurrences)"
        """

        # configs
        # configs = readConfig()

        # get atlas
        # atlas = configs["galaxiasSettings"]["atlas"]
        atlas = "Australia"

        # check for scientificName, as users should check that they have the correct column names
        if "scientificName" not in list(self.occurrences.columns):
            raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")

        # get all info     
        species_checked = self.check_species_names(return_taxa=True)
        
        # merge the taxon information with the species information the user has provided
        if type(species_checked) is tuple:
            self.occurrences = pd.merge(self.occurrences, species_checked[1], left_on='scientificName', right_on='scientificName', how='left')
            self.occurrences = self.occurrences.rename(
                columns = {
                    'rank': 'taxonRank',
                    'classs': 'class'
                }
            )
        else:
            raise ValueError("Some species names are not correct - please generate a report to find out which ones.")

    def add_unique_occurrence_IDs(self,
                                  column_name="occurrenceID"):
        """
        Function that automatically adds unique IDs (in the form of uuids) to each of your occurrences.

        Parameters
        ----------
            ``column_name`` : ``str``
                String containing name of column you want to add.  Default is ``occurrenceID``

        Returns
        -------
            ``None``

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.add_unique_occurrence_IDs()
            my_dwca.occurrences

        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_unique_occurrence_IDs();print(my_dwca.occurrences)"
        """

        if self.occurrences is None:
            raise ValueError("Please provide a data frame.")
        
        if column_name == "occurrenceID" or column_name == "catalogNumber" or column_name == "recordNumber":
            uuids = [None for i in range(self.occurrences.shape[0])]
            for i in range(self.occurrences.shape[0]):
                uuids[i] = str(uuid.uuid4())
            self.occurrences.insert(0,column_name,uuids)
            return self.occurrences
        else:
            raise ValueError("Please provide a string with a valid DwCA value for your column name.")

    def check_species_names(self,
                            return_taxa = False,
                            num_matches = 5,
                            include_synonyms = True):
        """
        Checks species names against your specified backbone.  Can also give you higher taxon ranks for your taxon.

        Parameters
        ----------
            ``return_taxa`` : ``logical``
                Option whether to return a dictionary object containing full taxonomic information on your species.  Default to `False`. 

        Returns
        -------
            Either ``False`` if there are incorrect taxon names, or ``True``.  A dictionary object containing species names and alternatives 
            is returned with the ``return_taxa=True`` option.

        Examples
        --------
        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc_rename.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.check_species_names()

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc_rename.csv\\\");my_dwca = galaxias.dwca(occurrences=data);print(my_dwca.check_species_names())"
        """

        # get configurations from user
        # configs = readConfig()

        # get atlas
        # atlas = configs["galaxiasSettings"]["atlas"]
        atlas = "Australia"

        # check for scientificName, as users should check that they have the correct column names
        if "scientificName" not in list(self.occurrences.columns):
            raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")
        
        # make a list of all scientific names in the dataframe
        scientific_names_list = list(set(self.occurrences["scientificName"]))
        
        # initialise has_invalid_taxa
        has_invalid_taxa=False
        
        # send list of scientific names to ALA to check their validity
        payload = [{"scientificName": name} for name in scientific_names_list]
        response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
        response_json = response.json()
        terms = ["original name"] + ["proposed match(es)"] + ["rank of proposed match(es)"] + TAXON_TERMS["Australia"]
        invalid_taxon_dict = {x: [] for x in terms}
        
        # loop over list of names and ensure we have gotten all the issues - might need to do single name search
        # to ensure we get everything
        for item in scientific_names_list:
            item_index = next((index for (index, d) in enumerate(response_json) if "scientificName" in d and d["scientificName"] == item), None)
            if item_index is None:
                # make this better
                has_invalid_taxa = True
                response_single = requests.get("https://api.ala.org.au/namematching/api/autocomplete?q={}&max={}&includeSynonyms={}".format("%20".join(item.split(" ")),num_matches,str(include_synonyms).lower()))
                response_json_single = response_single.json()
                if response_json_single:
                    if response_json_single[0]['rank'] is not None:
                        invalid_taxon_dict["original name"].append(item)
                        invalid_taxon_dict["proposed match(es)"].append(response_json_single[0]['name'])
                        invalid_taxon_dict["rank of proposed match(es)"].append(response_json_single[0]['rank'])
                        for term in TAXON_TERMS["Australia"]:
                            if term in response_json_single[0]['cl']:
                                invalid_taxon_dict[term].append(response_json_single[0]['cl'][term])
                            else:
                                invalid_taxon_dict[term].append(None)
                    else:

                        # check for synonyms
                        for synonym in response_json_single[0]["synonymMatch"]:
                            if synonym['rank'] is not None:
                                invalid_taxon_dict["original name"].append(item)
                                invalid_taxon_dict["proposed match(es)"].append(synonym['name'])
                                invalid_taxon_dict["rank of proposed match(es)"].append(synonym['rank'])
                                for term in TAXON_TERMS["Australia"]:
                                    if term in synonym['cl']:
                                        invalid_taxon_dict[term].append(synonym['cl'][term])
                                else:
                                    invalid_taxon_dict[term].append(None)
                            else:
                                print("synonym doesn't match")
                else:

                    # try one last time to find a match
                    response_search = requests.get("https://api.ala.org.au/namematching/api/search?q={}".format("%20".join(item.split(" "))))
                    response_search_json = response_search.json()            
                    if response_search_json['success']:
                        invalid_taxon_dict["original name"].append(item)
                        invalid_taxon_dict["proposed match(es)"].append(response_search_json['scientificName'])
                        invalid_taxon_dict["rank of proposed match(es)"].append(response_search_json['rank'])
                        for term in TAXON_TERMS["Australia"]:
                            if term in response_search_json:
                                invalid_taxon_dict[term].append(response_search_json[term])
                            else:
                                invalid_taxon_dict[term].append(None)
                    else:
                        print("last ditch search did not work")
                        print(response_search_json)
                        import sys
                        sys.exit()
            
        # check for homonyms - if there are any, then print them out to the user so the user can disambiguate the names
        if has_invalid_taxa:
            return False,pd.DataFrame(invalid_taxon_dict)
        elif return_taxa:
            payload = [{"scientificName": name} for name in scientific_names_list]
            response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
            response_json = response.json()
            verification_list = {"scientificName": scientific_names_list, "issues": [None for i in range(len(scientific_names_list))]}
            taxonomy = pd.DataFrame({name: [None for i in range(len(scientific_names_list))] for name in TAXON_TERMS[atlas]})
            
            # loop over list of names and ensure we have gotten all the issues - might need to do single name search
            # to ensure we get everything
            for i,item in enumerate(scientific_names_list):
                item_index = next((index for (index, d) in enumerate(response_json) if "scientificName" in d and d["scientificName"] == item), None)
                taxonomy.loc[i,"scientificName"] = item
                if item_index is not None:
                    verification_list["issues"][i] = response_json[item_index]["issues"]
                    if return_taxa:
                        for term in TAXON_TERMS[atlas]:
                            if term in response_json[item_index]:
                                taxonomy.loc[i,term] = response_json[item_index][term]
            return True,taxonomy
        return True

    def check_dwca(self):

        # get all variables
        vars_dict = vars(self)
        self_vars = list(vars(self).keys())
        data_vars = [x for x in self_vars if 'xml' not in x and 'name' not in x and 'md' not in x]
        
        # determine what type of archive it is
        data_files = list(itemgetter(*data_vars)(vars_dict))
        
        # check for empty archive
        if all(type(x) == type(data_files[0]) for x in data_files):
            raise ValueError("You have no data in your DwCA.  Please at least add occurrences")

        # first, check for events
        if self.events is not None:
            events_pass = self.check_events()
            occurrences_pass = self.check_occurrences()

            if self.multimedia is not None:
                multimedia_pass = self.check_multimedia()
                if not multimedia_pass:
                    raise ValueError("You need to check your multimedia files to make sure they are DwC compliant.")

            if self.emof is not None:
                emof_pass = self.check_emof()
                if not emof_pass:
                    raise ValueError("You need to check your multimedia files to make sure they are DwC compliant.")
                
            if events_pass and occurrences_pass:
                if os.path.exists(self.meta_xml) and os.path.exists(self.meta_xml):
                    return True
                else:
                    raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')
            elif not events_pass:
                raise ValueError("You need to check your events to make sure they are DwC compliant.")
            elif not occurrences_pass:
                raise ValueError("You need to check your occurrences to make sure they are DwC compliant.")
            else:
                raise ValueError("You need to check your events and occurrences to make sure they are DwC compliant.")
        
        # next, check for occurrences
        elif self.occurrences is not None:
            
            occurrences_pass = self.check_occurrences()

            if self.multimedia is not None:
                multimedia_pass = self.check_multimedia()
                if not multimedia_pass:
                    raise ValueError("You need to check your multimedia files to make sure they are DwC compliant.")

            if occurrences_pass:
                if os.path.exists(self.meta_xml) and os.path.exists(self.meta_xml):
                    return True
                else:
                    raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')
            else:
                raise ValueError('Your occurrences are not formatted correctly.')

        else:
            return False

    def check_dwca_values(self):

        return True

    def check_events(self):

        required_columns = False

        # check for required columns
        if any(map(lambda v: v in required_columns_event, list(self.events.columns))):

            # check to see if we are missing any columns
            check_missing_fields = set(list(self.events.columns)).issuperset(required_columns_event)
            
            # check for any missing required fields
            if (not check_missing_fields) or (type(check_missing_fields) is not bool and len(check_missing_fields) > 0):
                print("You are missing {}".format(list(set(required_columns_event).difference(set(self.events.columns)))))
                return required_columns
            else:
                required_columns = True
        else:
            return required_columns
        
        # check for 
        event_ids_ok = self.check_unique_event_ids()
        
        if event_ids_ok and required_columns:
            return True
        elif not event_ids_ok:
            list_event_ids = list(self.events['eventID'])
            duplicates = [x for x in list_event_ids if list_event_ids.count(x) >= 2]
            print("There are some duplicate eventIDs: {}".format(duplicates))
            return False
        else:
            return False
        
    def check_emof(self):
        
        vocab_check = get_dwc_noncompliant_terms(dataframe = self.emof)
        if len(vocab_check) > 0:
            raise ValueError("Your column names do not comply with the DwC standard: {}".format(vocab_check))
        
        return True

    def check_multimedia(self):
        
        vocab_check = get_dwc_noncompliant_terms(dataframe = self.multimedia)
        if len(vocab_check) > 0:
            raise ValueError("Your column names do not comply with the DwC standard: {}".format(vocab_check))
               
        return True
    
    def check_occurrences(self):

        # run basic checks
        vocab_check = get_dwc_noncompliant_terms(dataframe = self.occurrences)
        if len(vocab_check) > 0:
            raise ValueError("Your column names do not comply with the DwC standard.")
        
        # TODO: check all values in vocab are there
        values_check = self.check_dwca_values()
        if type(values_check) is not bool:
            raise ValueError("The values in some of your columns do not comply with the DwC standard.")
        
        # check for presence of occurrenceID
        if 'occurrenceID' not in list(self.occurrences):
            raise ValueError("You need to add unique identifiers into your occurrences.")
        
        # check for unique ids
        unique_id_check = self.check_unique_occurrence_ids()
        if not unique_id_check:
            list_event_ids = list(self.events['occurrenceID'])
            duplicates = [x for x in list_event_ids if list_event_ids.count(x) >= 2]
            raise ValueError("There are some duplicate eventIDs: {}".format(duplicates))
        
        return True

    def check_unique_event_ids(self):

        if len(list(set(self.events['eventID']))) < len(list(self.events['eventID'])):
            return False
        else:
            return True

    def check_unique_occurrence_ids(self):

        all_unique=False
        list_terms = list(self.occurrences.columns)
        unique_id_columns = ['occurrenceID','catalogNumber','recordNumber']
        for id in unique_id_columns:
            if id in list_terms:
                if len(list(set(self.occurrences[id]))) < len(list(self.occurrences[id])):
                    return False
                else:
                    all_unique =  True
        return all_unique
    
    def check_xmls(self):

        try:
            check = xmlschema.validate(self.eml_xml, 'http://rs.gbif.org/schema/eml-gbif-profile/1.1/eml-gbif-profile.xsd')
            return check
        except xmlschema.validators.exceptions.XMLSchemaChildrenValidationError as e:
            print("children error")
            print("There is an error with your eml.xml file:\n")
            if "value doesn't match any pattern of" in e.reason:
                value = str(e.elem).split(" ")[1]
                print("Please provide a value to {}".format(value))
                print()
            else:
                print(e.reason)
            breakpoint
        except xmlschema.validators.exceptions.XMLSchemaValidationError as e:
            print("schema validation")
            print("There is an error with your eml.xml file:\n")
            if "value doesn't match any pattern of" in e.reason:
                value = str(e.elem).split(" ")[1]
                print("Please provide a value to {}".format(value))
                print()
            elif "character data between child elements not allowed" in e.reason:
                value = str(e.elem).split(" ")[1]
                print("Please remove the value you've provided for {}".format(value))
                print()
            else:
                print(str(e.elem).split(" ")[1])
                print(e.reason)
            breakpoint

    
    def create_dwca(self):
        """
        create dwca 
        """
        # run basic checks on data
        data_check = self.check_dwca()

        # run xml check
        xml_check = self.check_xmls()
        if xml_check is None:
            xml_check = True
        
        if data_check and xml_check:
        
            # zip everything into file
            if self.events is not None:
                
                # open archive
                zf = zipfile.ZipFile(self.dwca_name,'w')

                # check if your data file has been written
                if not os.path.exists(self.occurrences_dwc_filename):
                    self.occurrences.to_csv("{}".format(self.occurrences_dwc_filename))

                # first, write occurrences
                occ_compression_opts = dict(method='zip',
                                            archive_name=self.occurrences_dwc_filename)             
                self.occurrences.to_csv(self.dwca_name,compression=occ_compression_opts)

                # check if your data file has been written
                if not os.path.exists(self.events_dwc_filename):
                    self.events.to_csv("{}".format(self.events_dwc_filename))

                # then, write multimedia if it exists
                events_compression_opts = dict(method='zip',
                                            archive_name=self.events_dwc_filename)             
                self.events.to_csv(self.dwca_name,compression=events_compression_opts)

                # then, write multimedia if it exists
                if self.multimedia is not None:

                    # check if data exists on disk
                    if not os.path.exists(self.multimedia_dwc_filename):
                        self.multimedia.to_csv("{}".format(self.multimedia_dwc_filename))
                    
                    # write to dwca
                    mm_compression_opts = dict(method='zip',
                                            archive_name=self.multimedia_dwc_filename)             
                    self.multimedia.to_csv(self.dwca_name,compression=mm_compression_opts)

                # then, write multimedia if it exists
                if self.emof is not None:
                    
                    # check if data exists on disk
                    if not os.path.exists(self.emof_dwc_filename):
                        self.emof.to_csv("{}".format(self.emof_dwc_filename))
                    
                    # write to dwca
                    emof_compression_opts = dict(method='zip',
                                                archive_name=self.emof_dwc_filename)             
                    self.emof.to_csv(self.dwca_name,compression=emof_compression_opts)

            else:
                
                # open archive
                zf = zipfile.ZipFile(self.dwca_name,'w')

                # check if your data file has been written
                if not os.path.exists(self.occurrences_dwc_filename):
                    self.occurrences.to_csv("{}".format(self.occurrences_dwc_filename))

                # first, write occurrences
                occ_compression_opts = dict(method='zip',
                                            archive_name=self.occurrences_dwc_filename)         
                self.occurrences.to_csv(self.dwca_name,compression=occ_compression_opts)

                # then, write multimedia if it exists
                if self.multimedia is not None:
                    if not os.path.exists(self.multimedia_dwc_filename):
                        self.multimedia.to_csv("{}".format(self.multimedia_dwc_filename))
                    mm_compression_opts = dict(method='zip',
                                                archive_name=self.multimedia_dwc_filename)             
                    self.multimedia.to_csv(self.dwca_name,compression=mm_compression_opts)

            # ensure metadata files are there
            if os.path.exists(self.meta_xml):
                zf.write(self.meta_xml)
            else:
                raise ValueError("You need to create your metadata files (eml.xml and meta.xml) - use the function make_meta_xml().")        
            
            if os.path.exists(self.eml_xml):
                zf.write(self.eml_xml)
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

    # def generate_data_report(self,
    #                          verbose=False,
    #                          ):
    #     """
    #     Generate a report for the data you will submit.  This currently prints out to screen, but will also
    #     render to HTML/MD (eventually)

    #     Parameters
    #     ----------
    #         ``verbose`` : ``logical``
    #             Option whether to generate a simple or verbose report.  Default to ``False``. 

    #     Returns
    #     -------
    #         A printed report detailing what will need to be edited prior to data submission.

    #     Examples
    #     --------
    #     .. prompt:: python

    #         import galaxias
    #         import pandas as pd
    #         data = pd.read_csv("occurrences_dwc.csv")
    #         my_dwca = galaxias.dwca(occurrences=data)
    #         my_dwca.generate_data_report()

    #     .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.generate_data_report()"
        
    #     """

    #     # get validation report
    #     if self.occurrences is not None:
            
    #         occurrences_validation_report = validate_occurrence_dataframe(self.occurrences)

    #     else:

    #         raise ValueError("You need occurrences to be able to run validation")

    #     # next, check for events
    #     if self.events is not None:
    #         events_validation_report = validate_event_dataframe(self.events) #,data_type="event")

    #         if self.emof is not None:
    #             emof_validation_report = validate_emof_extension(self.emof)
            
    #         else:
    #             emof_validation_report = None
        
    #     else:
    #         events_validation_report = None
    #         emof_validation_report = None

    #     # finally, check for multimedia
    #     if self.multimedia is not None:
    #         multimedia_validation_report = validate_media_extension(self.multimedia,data_type="occurrence")
    #     else:
    #         multimedia_validation_report = None

    #     # generate simple or complex report
    #     dwca_report(occurrence_report=occurrences_validation_report,
    #                 multimedia_report=multimedia_validation_report,
    #                 events_report=events_validation_report,
    #                 emof_report=emof_validation_report,
    #                 verbose=verbose)
    
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
        
        # get dwc terms
        dwc_terms_info = read_dwc_terms_links()

        if len(list(set(list(self.occurrences.columns)).intersection(list(dwc_terms_info['name'])))) < self.occurrences.shape[1]:
            raise ValueError("You are still missing some DwCA Terms.")

        # initialise metadata
        metadata = ET.Element("archive")
        metadata.set('xmlns', 'http://rs.tdwg.org/dwc/text/')
        metadata.set('metadata',self.eml_xml)

        # set the core of the archive and for
        core = ET.SubElement(metadata,"core")

        # check if it is an eventCore or an occurrenceCore
        if self.events is not None:
            core = build_subelement(element=core,
                                    row_type='http://rs.tdwg.org/dwc/terms/Event',
                                    filename=self.events_dwc_filename,
                                    data=self.events,
                                    dwc_terms_info=dwc_terms_info)
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                    filename=self.occurrences_dwc_filename,
                                    data=self.occurrences,
                                    dwc_terms_info=dwc_terms_info)
        else:
            core = build_subelement(element=core,
                                    row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                    filename=self.occurrences_dwc_filename,
                                    data=self.occurrences,
                                    dwc_terms_info=dwc_terms_info)

        ### TODO: write capability for extensions
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
                                    filename=self.multimedia_dwc_filename,
                                    data=self.emof,
                                    dwc_terms_info=dwc_terms_info)

        # write metadata
        tree = ET.ElementTree(metadata)
        ET.indent(tree, space="\t", level=0)
        tree.write(self.meta_xml, xml_declaration=True)
        
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
        with open(self.eml_xml, 'w') as f:
            f.write(xml_str)

def build_subelement(element=None,
                     row_type=None,
                     filename=None,
                     data=None,
                     dwc_terms_info=None):
    
    # set all basic elemnt things
    element.set("rowType",row_type)
    element.set("encoding","UTF-8")
    element.set("fieldsTerminatedBy",",") # CHANGE THIS TO WHATEVER OCCURRENCE IS
    element.set("linesTerminatedBy","\r\n") 
    element.set("fieldsEnclosedBy","&quot;")
    element.set("ignoreHeaderLines","1")

    # set locations of occurrence data
    element_files = ET.SubElement(element,"files")
    location = ET.SubElement(element_files,filename)

    # set id
    id = ET.SubElement(element,"id")
    id.set("index","0")

    # set all fields
    for i,fields in enumerate(list(data.columns)):
        field = ET.SubElement(element,"field")
        field.set("index","{}".format(i))
        index = dwc_terms_info[dwc_terms_info['name'] == fields]['link'].index[0]
        field.set("term",dwc_terms_info[dwc_terms_info['name'] == fields]['link'][index])

    # return element
    return element