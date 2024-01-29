import pandas as pd
import difflib
import os
from .galaxias_config import readConfig
from .dwca_report import dwca_report
import difflib
import json
import uuid
import requests
import jsonpickle
import datetime
from .common_dictionaries import REQUIRED_DWCA_TERMS,NAME_MATCHING_TERMS,ID_REQUIRED_DWCA_TERMS
from .common_dictionaries import GEO_REQUIRED_DWCA_TERMS,TAXON_TERMS
from dwc_validator.validate import validate_occurrence_dataframe,create_taxonomy_report

# testing
import sys

class dwca:

    def __init__(self,
                 occurrences: pd.core.frame.DataFrame = None,
                 dwca_name: str = "dwca.zip",
                 data_type: str="Occurrence",
                 metadata_md: str = None,
                 eml_xml: str = None,
                 meta_xml: str = None
                 ):
        
        # check for if user provides data frame 
        if dwca_name != "dwca.zip":
            self.dwca_name = dwca_name
        if occurrences is not None and type(occurrences) is pd.core.frame.DataFrame:
            self.occurrences = occurrences
        else:
            print("WARNING: if your occurrences argument is not a dataframe, occurrences will be set to None")
            self.occurrences = None

        # check for what type of DwCA it iwll be
        if data_type in ["Occurrence","Event","Media"]:
            self.data_type = data_type
        else:
            raise ValueError("galaxias only takes occurrence and event DwC data at this time.")
        if metadata_md is None and eml_xml is None and meta_xml is None:
            metadata_md = self.create_metadata_file()
            self.add_metadata_md(metadata_md=metadata_md)
        self.eml_xml = eml_xml
        self.meta_xml = meta_xml

    def add_metadata_md(self,
                        metadata_md=None):
        """
        adds a markdown file to your ``dwca`` object.  This is for if you have your own custom 

        Parameters
        ----------
            metadata_md: ``str``
                ``str`` containing the name of the metadata markdown file

        Returns
        -------
            None
        """
        if metadata_md is None:
            raise ValueError("Please provide a valid path to and name for the metadata markdown file.")
        
        self.metadata_md = metadata_md

    def add_taxonomic_information(self):
        """
        Adds full taxonomic information (from kingdom to species) to your data for clearer identification

        Parameters
        ----------
            None

        Returns
        -------
            None

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.add_taxonomic_information()
            my_dwca.occurrences
            
        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"data.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_taxonomic_information();print(my_dwca.occurrences)"
        """

        # configs
        configs = readConfig()

        # get atlas
        atlas = configs["galaxiasSettings"]["atlas"]

        # check for scientificName, as users should check that they have the correct column names
        if "scientificName" not in list(self.occurrences.columns):
            raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")

        # get all info     
        species_checked = self.check_species_names(return_taxa=True)
        
        # merge the taxon information with the species information the user has provided
        if type(species_checked) is tuple:
            self.occurrences = pd.merge(self.occurrences, species_checked[1], left_on='scientificName', right_on='scientificName', how='left')
            self.occurrences.rename(
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
            column_name : ``str``
                String containing name of column you want to add.  Default is "occurrenceID"

        Returns
        -------
            ``None``

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.add_unique_occurrence_IDs()
            my_dwca.occurrences

        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"data.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_unique_occurrence_IDs();print(my_dwca.occurrences)"
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
                            return_taxa = False):
        """
        Checks species names against your specified backbone.  Can also give you higher taxon ranks for your taxon.

        Parameters
        ----------
            return_taxa : logical
                Option whether to return a dictionary object containing full taxonomic information on your species.  Default to `False`. 

        Returns
        -------
            Either `False` if there are incorrect taxon names, or `True`.  A dictionary object containing species names and alternatives
            is return with the ``return_taxa=True`` option.

        Examples
        --------
        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.check_species_names()

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\\\"data.csv\\\");my_dwca = galaxias.dwca(occurrences=data);print(my_dwca.check_species_names())"
        """

        # get configurations from user
        configs = readConfig()

        # get atlas
        atlas = configs["galaxiasSettings"]["atlas"]

        # check for scientificName, as users should check that they have the correct column names
        if "scientificName" not in list(self.occurrences.columns):
            raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")
        
        # make a list of all scientific names in the dataframe
        scientific_names_list = list(set(self.occurrences["scientificName"]))
        
        # send list of scientific names to ALA to check their validity
        payload = [{"scientificName": name} for name in scientific_names_list]
        response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
        response_json = response.json()
        verification_list = {"scientificName": scientific_names_list, "issues": [None for i in range(len(scientific_names_list))]}
        taxonomy = pd.DataFrame({name: [None for i in range(len(scientific_names_list))] for name in TAXON_TERMS[atlas]})
        
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
            
        # check for homonyms - if there are any, then print them out to the user so the user can disambiguate the names
        df_verification = pd.DataFrame(verification_list)
        df_isnull = df_verification.loc[df_verification['issues'].astype(str).str.contains("homonym",case=False,na=False)]
        if not df_isnull.empty:
            return False
        elif return_taxa:
            return True,pd.DataFrame(taxonomy)
        return True
    
    # def create_dwca(self):
    #     """
    #     create dwca 
    #     """
    #     n=1

    def create_metadata_file(self,
                             filename = None,
                             path = "."):
        
        """
        Create a markdown file for the user to edit
        """
        
        if filename is not None:
            parts = filename.split("/")
            path = "/".join(parts[:-1])
        if not os.path.exists(path + '/metadata.md'):
            # print("Generating markdown file in working directory ({}) for metadata...".format(path))
            os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),os.path.join(path,"metadata.md")))
        else:
            pass
            # print("You already have a metadata.md file.")
        return path + "/metadata.md"

    def generate_data_report(self,
                             verbose=False,
                             ):
        """
        Generate a report for the data you will submit.  This currently prints out to screen, but will also
        render to HTML/MD (eventually)

        Parameters
        ----------
            verbose : logical
                Option whether to generate a simple or verbose report.  Default to `False`. 

        Returns
        -------
            A printed report detailing what will need to be edited to be able to submit your data.

        Examples
        --------
        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("data.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.generate_data_report()

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\\\"data.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.generate_data_report()"
        
        """
        
        # get validation report
        validation_report = validate_occurrence_dataframe(self.occurrences)

        # generate simple or complex report
        dwca_report(report=validation_report,verbose=verbose)

    def convert_coordinates(self,
                            latitude_column_name = None,
                            longitude_column_name = None):

        if latitude_column_name is None:
            raise ValueError("Please provide a name for your latitude column bame")

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

    # def rename_dwc_columns(self,
    #                        names=None):
    #     """
    #     Renames all columns in the data to names that are Darwin Core Archive compliant.

    #     Parameters
    #     ----------
    #         dataframe : `pandas` dataframe
    #             Dataframe containing species name you want to turn into a Darwin Core Archive.
    #         names : dict
    #             Dictionary containing pairwise relationships between old column names and new column names, i.e. {"species":"scientificName"} 

    #     Returns
    #     -------
    #         `pandas` dataframe with renamed columns

    #     Examples
    #     --------

    #     .. prompt:: python

    #         import galaxias
    #         import pandas as pd
    #         data = pd.read_csv("data_wrong_names.csv")
    #         data.columns
    #         data_new = galaxias.rename_column_names(dataframe=data,names={})
    #         data_new.columns

    #     #.. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\"data_wrong_names.csv\");print(data.columns);data_new = galaxias.rename_column_names(dataframe=data,names={});print(data_new.columns)"
    #     """

    #     if names is not None:

    #         # add another column to specify rank if species is in column name
    #         # if any("species" in key for key in self.occurrence_data.keys()):
    #         #     index = [i for i,name in enumerate(self.occurrence_data.columns) if "species" in name.lower()][0]
    #         #     self.occurrences.insert(loc=index,column="rank",value="species") 
            
    #         # rename columns to comply with dwc standards
    #         self.occurrences = self.occurrences.rename(names,axis=1)
            
    #     else:

    #         raise ValueError("Please provide a dataframe, as well as a dictionary of current and desired names.")
