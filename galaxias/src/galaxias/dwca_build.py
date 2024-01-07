import pandas as pd
import difflib
import os
from .metadata import read_dwc_terms
from .galaxias_config import readConfig
from .dwca_report import dwca_report
import difflib
import json
import uuid
import requests
import jsonpickle
from .common_dictionaries import REQUIRED_DWCA_TERMS,NAME_MATCHING_TERMS,ID_REQUIRED_DWCA_TERMS
from .common_dictionaries import GEO_REQUIRED_DWCA_TERMS,TAXON_TERMS
from dwc_validator.validate import validate_occurrence_dataframe

# testing
import sys

class dwca:

    def __init__(self,
                 dataframe: pd.core.frame.DataFrame = None,
                 filename: str = None,
                 occurrence_data: bool = True,
                 event_data: bool = False,
                 metadata_md: str = None,
                 eml_xml: str = None,
                 meta_xml: str = None
                 ):
        
        # check for if user provides data frame 
        if filename is not None:
            self.dataframe = pd.read_csv(filename)
        else:
            self.dataframe = pd.DataFrame(dataframe)
        if occurrence_data:
            self.data_type = "Occurrence"
        elif event_data:
            self.data_type = "Event"
        else:
            raise ValueError("galaxias only takes occurrence and event DwC data at this time.")
        if metadata_md is None and eml_xml is None and meta_xml is None:
            metadata_md = self.create_metadata_file(filename = filename)
            self.add_metadata_md(metadata_md=metadata_md)
        self.eml_xml = eml_xml
        self.meta_xml = meta_xml
    
    # def create_dwca(self):
    #     """
    #     create dwca 
    #     """
    #     n=1

    def add_metadata_md(self,
                        metadata_md=None):
        """
        add metadata file to the object for later creation of xmls and dwcas
        """
        if metadata_md is None:
            raise ValueError("Please provide a valid path to and name for the metadata markdown file.")
        
        self.metadata_md = metadata_md

    def generate_data_report(self,
                             verbose=False,
                             ):
        """
        generate report for your data frame
        """
        
        # get validation report
        validation_report = validate_occurrence_dataframe(self.dataframe)

        # generate simple or complex report
        dwca_report(report=validation_report,verbose=verbose)

    def create_metadata_file(self,
                             filename = None,
                             path = "."):
        '''Create a markdown file for the user to edit'''
        if filename is not None:
            parts = filename.split("/")
            path = "/".join(parts[:-1])
        if not os.path.exists(path + '/metadata.md'):
            print("Generating markdown file in working directory ({}) for metadata...".format(path))
            os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),os.path.join(path,"metadata.md")))
        else:
            print("You already have a metadata.md file.")
        return path + "/metadata.md"

    # def check_dwca_column_names_valid(self,
    #                                   return_invalid_values=False):
    #     """
    #     Check all Darwin Core column names and provides alternatives to ones that are incorrect/invalid.  It also checks for any required DwCA
    #     terms for the atlas you are choosing to submit your data to.

    #     Parameters
    #     ----------
    #         dataframe : `pandas` dataframe
    #             Dataframe containing species occurrence records you want to turn into a Darwin Core Archive. 
    #         return_invalid_values : logical
    #             choose whether or not to return all invalid and missing values as a list or to print to screen.  Default to `False` and will print to screen.

    #     Returns
    #     -------
    #         Either `True`, `False` or a dictionary object containing species names and alternatives.

    #     Examples
    #     --------

    #     This example is a dataframe that contains the incorrect DwCA terms for X, Y and Z.

    #     .. prompt:: python

    #         import galaxias
    #         import pandas as pd
    #         data = pd.read_csv("data_wrong_names.csv")
    #         galaxias.check_dwca_column_names_valid(dataframe=data)

    #     .. program-output:: python -c "import galaxias;import pandas as pd; data = pd.read_csv(\"tests/data_wrong_names.csv\");galaxias.check_dwca_column_names_valid(dataframe=data)"
        
    #     This example is a dataframe that contains all valid DwCA terms.

    #     .. prompt:: python

    #         import galaxias
    #         import pandas as pd
    #         data = pd.read_csv("data_correct_names.csv")
    #         galaxias.check_dwca_column_names_valid(dataframe=data)

    #     .. program-output:: python -c "import galaxias;import pandas as pd; data = pd.read_csv(\"tests/data_correct_names.csv\");galaxias.check_dwca_column_names_valid(dataframe=data)"
        
    #     """

    #     # get configurations
    #     configs = readConfig()

    #     # get atlas
    #     atlas = configs["galaxiasSettings"]["atlas"]

    #     # get all dwc terms to validate against
    #     dwc_terms_df = read_dwc_terms()
    #     dwc_terms = list(dwc_terms_df['term'])

    #     # get column names of data frame and check if the columns are compatible with current dwca terms
    #     column_names = list(self.occurrence_data)
    #     bool_list = list(map(lambda v: v in dwc_terms, column_names))

    #     # check for required columns for chosen atlas
    #     missing_requirements = []
    #     check_required_dwca_terms = list(map(lambda v: v in column_names, REQUIRED_DWCA_TERMS[atlas]))
    #     for check,term in zip(check_required_dwca_terms,REQUIRED_DWCA_TERMS[atlas]):
    #         if not check:
    #             missing_requirements.append(term)
    #     check_id_required_dwca_terms = list(map(lambda v: v in column_names,ID_REQUIRED_DWCA_TERMS[atlas]))
    #     if not any(check_id_required_dwca_terms):
    #         missing_requirements.append(ID_REQUIRED_DWCA_TERMS[atlas][0])
    #     check_geo_required_dwca_terms = list(map(lambda v: v in column_names,GEO_REQUIRED_DWCA_TERMS[atlas]))
    #     missing_geo_requirements = []
    #     for check,term in zip(check_geo_required_dwca_terms,GEO_REQUIRED_DWCA_TERMS[atlas]):
    #         if not check:
    #             missing_geo_requirements.append(term)
    #     invalid_dwca_terms = {}

    #     # check if column names are valid dwc terms, and if not, provide the closest suggestions
    #     # either return the lists of terms that are incorrect, or print them to screen for user
    #     if (not all(bool_list)) or len(missing_geo_requirements) > 0 or len(missing_requirements) > 0:
    #         for name,check in zip(column_names,bool_list):
    #             if check is False:
    #                 if "species" in name.lower():
    #                     invalid_dwca_terms[name] = difflib.get_close_matches("scientific",dwc_terms)
    #                 elif "date" in name.lower():
    #                     invalid_dwca_terms[name] = difflib.get_close_matches("eventDate",dwc_terms)
    #                     invalid_dwca_terms[name] += difflib.get_close_matches("date",dwc_terms)
    #                     invalid_dwca_terms[name] += (difflib.get_close_matches(name,dwc_terms))
    #                 elif "site" in name.lower():
    #                     invalid_dwca_terms[name] = difflib.get_close_matches("locat",dwc_terms)
    #                 else:
    #                     invalid_dwca_terms[name] = difflib.get_close_matches(name,dwc_terms)
    #         if return_invalid_values:
    #             return invalid_dwca_terms,missing_requirements,missing_geo_requirements
    #         else:
    #             print("The following are all invalid DarwinCore terms, and the closest suggestions follow:")
    #             for key in invalid_dwca_terms:
    #                 print("{}: {}".format(key,invalid_dwca_terms[key]))
    #             print("\nYou are missing these required fields.  These may not exist in the data, or need their title changed.\n")
    #             for key in missing_requirements:
    #                 print(key)
    #             if "decimalLatitude" not in column_names or "decimalLongitude" not in column_names or "geodeticDatum" not in column_names or "coordinateUncertaintyInMeters" not in column_names:
    #                 print("\nYou are missing the following geospatial requirements:\n")
    #                 for key in missing_geo_requirements:
    #                     print(key)
    #             else:
    #                 print("\nYou might be missing geospatial requirements:\n")
    #                 for key in missing_geo_requirements:
    #                     print(key)
    #             return False
    #     return True


    # def check_for_duplicate_column_names(self):
    #     """
    #     Check all Darwin Core column names and see if there are any duplicates.

    #     Parameters
    #     ----------
    #         self : `dwca` object
    #             `dwca` object you added data tp amd wamt  

    #     Returns
    #     -------
    #         Logical dictating if the data frame passed.

    #     Examples
    #     --------

    #     Here is an example of having duplicate column names.

    #     .. prompt:: python

    #         import galaxias
    #         import pandas as pd
    #         data = pd.read_csv("data_duplicate_names.csv")
    #         galaxias.check_dwca_column_names_valid(dataframe=data)
            
    #     .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_duplicate_names.csv\");galaxias.check_dwca_column_names_valid(dataframe=data)"
        
    #     Here is an example of not having duplicate column names.

    #     .. prompt:: python

    #         import galaxias
    #         import pandas as pd
    #         data = pd.read_csv("data_no_duplicate_names.csv")
    #         galaxias.check_dwca_column_names_valid(dataframe=data)
            
    #     .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"ddata_no_duplicate_names.csv\");galaxias.check_dwca_column_names_valid(dataframe=data)"
    #     """
    #     print(self)
    #     columns = list(self.occurrence_data.columns)
    #     set_columns = set(columns)
    #     if len(set_columns) < len(columns):
    #         return False
    #     return True
    
    # def check_for_duplicate_records(self):
    #     """
    #     checking for duplicate records in the data
    #     """
    #     duplicate_rows = self.occurrence_data[self.occurrence_data.duplicated()]
    #     if duplicate_rows is not None:
    #         return False
    #     return True

    def rename_dwc_columns(self,
                           names=None):
        """
        Renames all columns in the data to names that are Darwin Core Archive compliant.

        Parameters
        ----------
            dataframe : `pandas` dataframe
                Dataframe containing species name you want to turn into a Darwin Core Archive.
            names : dict
                Dictionary containing pairwise relationships between old column names and new column names, i.e. {"species":"scientificName"} 

        Returns
        -------
            `pandas` dataframe with renamed columns

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data_wrong_names.csv")
            data.columns
            data_new = galaxias.rename_column_names(dataframe=data,names={})
            data_new.columns

        #.. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_wrong_names.csv\");print(data.columns);data_new = galaxias.rename_column_names(dataframe=data,names={});print(data_new.columns)"
        """

        if names is not None:

            # add another column to specify rank if species is in column name
            # if any("species" in key for key in self.occurrence_data.keys()):
            #     index = [i for i,name in enumerate(self.occurrence_data.columns) if "species" in name.lower()][0]
            #     self.dataframe.insert(loc=index,column="rank",value="species") 
            
            # rename columns to comply with dwc standards
            self.dataframe = self.dataframe.rename(names,axis=1)
            
        else:

            raise ValueError("Please provide a dataframe, as well as a dictionary of current and desired names.")

    def check_species_names(self,
                            num_matches=5,
                            include_synonyms=True,
                            return_matches = False,
                            return_taxa = False,
                            replace_old_names = False):
        """
        Checks species names against the ALA repository.  Provides alternatives for ones that are homonyms or are not in the database.

        Parameters
        ----------
            dataframe : `pandas` dataframe
                Dataframe containing species name you want to turn into a Darwin Core Archive. 
            num_matches : int
                Number of matching names you want to be provided in case there is a mismatched name.  Default to 5. 
            include_synonyms : logical
                Includes possible synonyms for your species. Default to `True`.
            return_matches : logical
                Option whether to return a dictionary object containing species names and alternatives.  Default to `False`.  
            return_taxa : logical
                Option whether to return a dictionary object containing full taxonomic information on your species.  Default to `False`. 
            replace_old_names : logical
                Option whether to replace any outdated species names with the most recent taxonomic names.  Default to `False`. 

        Returns
        -------
            Either `True`, `False` or a dictionary object containing species names and alternatives.

        Examples
        --------
        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data_correct_species_names.csv")
            galaxias.check_species_names(dataframe=data,replace_old_names=True)

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_correct_species_names.csv\");galaxias.check_species_names(dataframe=new_data,replace_old_names=True)"

            import galaxias
            import pandas as pd
            data = pd.read_csv("data_incorrect_species_names.csv")
            galaxias.check_species_names(dataframe=data,replace_old_names=True)

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_incorrect_species_names.csv\");galaxias.check_species_names(dataframe=data,replace_old_names=True)"
        """

        # get configurations from user
        configs = readConfig()

        # get atlas
        atlas = configs["galaxiasSettings"]["atlas"]

        # check for scientificName, as users should check that they have the correct column names
        if "scientificName" not in list(dataframe.columns):
            raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")
        
        # make a list of all scientific names in the dataframe
        scientific_names_list = list(set(dataframe["scientificName"]))
        
        # send list of scientific names to ALA to check their validity
        payload = [{"scientificName": name} for name in scientific_names_list]
        response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
        response_json = response.json()
        verification_list = {"scientificName": scientific_names_list, "issues": [None for i in range(len(scientific_names_list))]}
        taxonomy = {name: [None for i in range(len(scientific_names_list))] for name in TAXON_TERMS[atlas]}
        
        # loop over list of names and ensure we have gotten all the issues - might need to do single name search
        # to ensure we get everything
        for i,item in enumerate(scientific_names_list):
            item_index = next((index for (index, d) in enumerate(response_json) if "scientificName" in d and d["scientificName"] == item), None)
            taxonomy["scientificName"][i] = item
            if item_index is not None:
                verification_list["issues"][i] = response_json[item_index]["issues"]
                if return_taxa:
                    for term in TAXON_TERMS[atlas]:
                        if term in response_json[item_index]:
                            taxonomy[term][i] = response_json[item_index][term]
            else:
                response_single = requests.get("https://api.ala.org.au/namematching/api/search?q={}".format("%20".join(item.split(" "))))
                response_json_single = response_single.json()
                if response_json_single['success']:
                    if response_json_single['scientificName'] == item:
                        verification_list["issues"][i] = response_json_single["issues"]
                        if return_taxa:
                            for term in TAXON_TERMS[atlas]:
                                if term in response_json_single:
                                    taxonomy[term][i] = response_json_single[term]
                    else:
                        if replace_old_names:
                            # replace old names with updated names
                            dataframe = self.change_species_names(dataframe=dataframe,species_changes={item: response_json_single["scientificName"]})
                        else:
                            verification_list["issues"][i] = "homonym"
                else:
                    verification_list["issues"][i] = response_json_single["issues"]

        # check for homonyms - if there are any, then print them out to the user so the user can disambiguate the names
        df_verification = pd.DataFrame(verification_list)
        df_isnull = df_verification.loc[df_verification['issues'].astype(str).str.contains("homonym",case=False,na=False)]
        if not df_isnull.empty:
            print("You have one or more invalid taxa in your data.  Invalid taxa are:\n")
            invalid_taxon = df_verification.loc[df_verification['issues'].astype(str).str.contains("homonym",case=False,na=False)]
            print(invalid_taxon)
            print("\nSuggested names are below:\n")
            matches = {x: None for x in invalid_taxon['scientificName']}
            for name in invalid_taxon['scientificName']:
                print(name)
                print()
                response = requests.get("https://api.ala.org.au/namematching/api/autocomplete?q={}&max={}&includeSynonyms={}".format("%20".join(name.split(" ")),num_matches,str(include_synonyms).lower()))
                data = {x: [] for x in NAME_MATCHING_TERMS[atlas]}
                response_json = response.json()
                list_names = [x["name"] for x in response_json]
                for item in list_names:
                    response_single = requests.get("https://api.ala.org.au/namematching/api/search?q={}".format("%20".join(item.split(" "))))
                    response_json_single = response_single.json()
                    names_df = pd.DataFrame()
                    if response_json_single['success']:
                        for item in NAME_MATCHING_TERMS[atlas]:
                            if item in response_json_single:
                                data[item].append(response_json_single[item])
                            else:
                                data[item].append(None)
                names_df = pd.DataFrame(data)
                if return_matches:
                    matches[name] = names_df
                print(names_df)
                print()
            if return_matches:
                return(matches)
            return False
        elif return_taxa:
            return True,pd.DataFrame(taxonomy)
        return True

    def add_column(self,
                   column_name=None,
                   value=None):
        """
        Checks the spatial validity of the data.  The ALA's data is represented as WGS84, so latitude and longitude should be in degrees.

        Parameters
        ----------
            dataframe : `pandas` dataframe
                Dataframe containing species name you want to turn into a Darwin Core Archive.

        Returns
        -------
            `True` if the data frame has spatially valid data, `False` if it does not.

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data_correct_lat_long.csv")
            galaxias.check_spatial_validity(dataframe=data)

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_correct_lat_long.csv\");galaxias.check_spatial_validity(dataframe=data)"
        """

        if self.dataframe is None:
            raise ValueError("Please provide a data frame.")
        
        # get dwca terms
        dwc_terms_df = read_dwc_terms()
        dwc_terms = list(dwc_terms_df['term'])

        if column_name is None:
            raise ValueError("Please provide a string with a valid DwCA value for your column name.")
        elif column_name == "occurrenceID" or column_name == "catalogNumber" or column_name == "recordNumber":
            uuids = [None for i in range(self.dataframe.shape[0])]
            for i in range(self.dataframe.shape[0]):
                uuids[i] = str(uuid.uuid4())
            self.dataframe[column_name] = uuids
            return self.dataframe
        elif column_name in dwc_terms:
            if value is None:
                raise ValueError("Please provide a default value for this column.")
            else:
                self.dataframe[column_name] = value
        else:
            raise ValueError("Please provide a string with a valid DwCA value for your column name.")
        
    def add_taxonomic_information(self):
        """
        Adds full taxonomic information (from kingdom to species) to your data for clearer identification

        Parameters
        ----------
            dataframe : `pandas` dataframe
                Dataframe containing species occurrence records you want to turn into a Darwin Core Archive.

        Returns
        -------
            `pandas` dataframe provided that now contains full taxonomic information.

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data_add_taxon_information.csv")
            data_taxon = galaxias.check_spatial_validity(dataframe=data)
            data_taxon.head()
            
        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_add_taxon_information.csv\");data_taxon = galaxias.check_spatial_validity(dataframe=data);print(data_taxon.head())"
        """

        # configs
        configs = readConfig()

        # get atlas
        atlas = configs["galaxiasSettings"]["atlas"]

        #if self.occurrence_data is None:
        #    raise ValueError("Please provide a dataframe to the function.")

        # check for scientificName, as users should check that they have the correct column names
        if "scientificName" not in list(self.dataframe.columns):
            raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")

        # get all info     
        species_checked,taxon_info = self.check_species_names(self,return_taxa=True)

        # merge the taxon information with the species information the user has provided
        if species_checked:
            taxon_dataframe = pd.merge(self.dataframe, taxon_info, left_on='scientificName', right_on='scientificName', how='left')
        else:
            taxon_dataframe = None

        # return the data frame to the user
        return taxon_dataframe

    def change_species_names(self,
                             species_changes=None):
        """
        Changes any species names that are incorrect/invalid/misidentified to the correct ones

        Parameters
        ----------
            dataframe : `pandas` dataframe
                Dataframe containing species occurrence records you want to turn into a Darwin Core Archive.
            species_changes : dict
                Dictionary containing existing species name in your data frame, as well as the new species name.
                
        Returns
        -------
            `pandas` dataframe provided that contains changed species name.

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data_change_species_names.csv")
            new_data_species_rename = galaxias.change_species_names(dataframe=data,species_changes={})
            new_data_species_rename.head()
            
        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_change_species_names.csv\");new_data_species_rename = galaxias.check_spatial_validity(dataframe=data,species_changes={});print(new_data_species_rename.head())"
        """
            
        if self.dataframe is None:
            raise ValueError("Please provide a dataframe to the function.")
        
        if species_changes is None:
            raise ValueError("Please provide a dictionary with the species names to change.")
        
        if "scientificName" not in self.dataframe:
            raise ValueError("Check your column names - scientificName is the title to use for species names.  If yours is something different, please change it to scientificName.")

        for species in species_changes:
            self.dataframe['scientificName'] = self.dataframe['scientificName'].replace(regex=species, value=species_changes[species])