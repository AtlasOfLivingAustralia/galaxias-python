import pandas as pd
import os
from .galaxias_config import readConfig
from .dwca_report import dwca_report
import json
import uuid
import requests
from .common_dictionaries import TAXON_TERMS
from dwc_validator.validate import validate_occurrence_dataframe,validate_media_extension
from dwc_validator.validate import validate_event_dataframe,validate_emof_extension
import xml.etree.ElementTree as ET

class dwca:

    def __init__(self,
                 occurrences: pd.core.frame.DataFrame = None,
                 occurrences_name = "occurrences.csv",
                 multimedia: pd.core.frame.DataFrame = None,
                 multimedia_name = "multimedia.csv",
                 events: pd.core.frame.DataFrame = None,
                 events_name = "events.csv",
                 emof: pd.core.frame.DataFrame = None,
                 emof_name = "extendedMeasurementOrFact.csv",
                 dwca_name: str = "dwca.zip",
                 metadata_md: str = None,
                 eml_xml: str = "eml.xml",
                 meta_xml: str = "meta.xml"
                 ):
        
        # check for if user provides data frame 
        if dwca_name != "dwca.zip":
            self.dwca_name = dwca_name

        # set occurrences first and foremost
        if occurrences is not None and type(occurrences) is pd.core.frame.DataFrame:
            self.occurrences = occurrences
        else:
            print("WARNING: if your occurrences argument is not a dataframe, occurrences will be set to None")
            self.occurrences = None

        # then, check for multimedia
        if multimedia is not None and type(multimedia) is pd.core.frame.DataFrame:
            self.multimedia = multimedia
        elif multimedia is None:
            self.multimedia=None
        else:
            raise ValueError("Only a pandas dataframe will be accepted for multimedia.")

        # then, check if it is an event core
        if events is not None and type(events) is pd.core.frame.DataFrame:
            self.events = events
        elif events is None:
            self.events=None
        else:
            raise ValueError("Only a pandas dataframe will be accepted for events.")
        
        # then, check if it is an event core
        if events is not None:
            if emof is not None and type(emof) is pd.core.frame.DataFrame:
                self.emof = emof
            elif emof is None:
                self.emof=None
            else:
                raise ValueError("Only a pandas dataframe will be accepted for extended measurement or fact.")

        # check for names of data files
        if occurrences_name is not None:
            self.occurrences_name = occurrences_name
        if multimedia_name is not None:
            self.occurrences_name = occurrences_name
        if events_name is not None:
            self.occurrences_name = occurrences_name
        if emof_name is not None:
            self.occurrences_name = occurrences_name

        # check for what type of DwCA it iwll be
        if metadata_md is None:
            metadata_md = self.create_metadata_file()
            self.metadata_md = metadata_md

        # set the eml and meta 
        self.eml_xml = eml_xml
        self.meta_xml = meta_xml

    def add_metadata_md(self,
                        metadata_md=None):
        """
        adds a markdown file to your ``dwca`` object.  This is for if you have your own custom 

        Parameters
        ----------
            ``metadata_md`` : ``str``
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
                            return_taxa = False):
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
            taxonomy.loc[i,"scientificName"] = item
            if item_index is not None:
                verification_list["issues"][i] = response_json[item_index]["issues"]
                if return_taxa:
                    for term in TAXON_TERMS[atlas]:
                        if term in response_json[item_index]:
                            taxonomy.loc[i,term] = response_json[item_index][term]
            
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
        
        if filename is not None:
            parts = filename.split("/")
            path = "/".join(parts[:-1])
        if not os.path.exists(path + '/metadata.md'):
            os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),os.path.join(path,"metadata.md")))
        else:
            pass
        return path + "/metadata.md"

    def generate_data_report(self,
                             verbose=False,
                             ):
        """
        Generate a report for the data you will submit.  This currently prints out to screen, but will also
        render to HTML/MD (eventually)

        Parameters
        ----------
            ``verbose`` : ``logical``
                Option whether to generate a simple or verbose report.  Default to ``False``. 

        Returns
        -------
            A printed report detailing what will need to be edited prior to data submission.

        Examples
        --------
        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.generate_data_report()

        .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.generate_data_report()"
        
        """

        # get validation report
        if self.occurrences is not None:
            
            occurrences_validation_report = validate_occurrence_dataframe(self.occurrences)

        else:

            raise ValueError("You need occurrences to be able to run validation")

        # next, check for events
        if self.events is not None:
            events_validation_report = validate_event_dataframe(self.events) #,data_type="event")

            if self.emof is not None:
                emof_validation_report = validate_emof_extension(self.emof)
            
            else:
                emof_validation_report = None
        
        else:
            events_validation_report = None
            emof_validation_report = None

        # finally, check for multimedia
        if self.multimedia is not None:
            multimedia_validation_report = validate_media_extension(self.multimedia,data_type="occurrence")
        else:
            multimedia_validation_report = None

        # generate simple or complex report
        dwca_report(occurrence_report=occurrences_validation_report,
                    multimedia_report=multimedia_validation_report,
                    events_report=events_validation_report,
                    emof_report=emof_validation_report,
                    verbose=verbose)
        
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
       
        # initialise the eml xml
        metadata = ET.Element("eml:eml")
        metadata.set('xmlns:d', 'eml://ecoinformatics.org/dataset-2.1.0')
        metadata.set('xmlns:eml', 'eml://ecoinformatics.org/eml-2.1.1')
        metadata.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        metadata.set('xmlns:dc', 'http://purl.org/dc/terms/')
        metadata.set('xsi:schemaLocation', 'eml://ecoinformatics.org/eml-2.1.1 http://rs.gbif.org/schema/eml-gbif-profile/1.1/eml-gbif-profile.xsd')
        metadata.set('system','ALA-Registry')
        metadata.set('scope','system')
        metadata.set('xml:lang','en')
        
        # initialise elements
        elements = {}

        # open the metadata file
        metadata_file = open(self.metadata_md, "r")

        # loop over things in metadata
        title = ""
        description = ""
        top_titles = []
        duplicate = 0
        for line in metadata_file:
            if line != "\n":
                if "#" == line[0]:
                    title = line.strip()
                elif "#" != line[0]:
                    if description != "":
                        description.append(line.strip())
                    else:
                        description = [line.strip()]
            elif line == "\n" and title != "" and description != "":
                if title not in elements:
                    elements[title] = description
                else:
                    elements["{}{}".format(title,duplicate)] = description
                    duplicate += 1
                if title.split(" ")[0] == "#":
                    top_titles.append(title)
                description = ""
                title = ""
            elif line == "\n" and title != "":
                if title not in elements:
                    elements[title] = ""
                else:
                    elements["{}{}".format(title,duplicate)] = ""
                    duplicate += 1
                if title.split(" ")[0] == "#":
                    top_titles.append(title)
                title = ""
        metadata_file.close()

        # build a tree
        title_list = [key for key in elements]

        # stuff
        top_title_indices = [i for i, j in enumerate(title_list) if j in top_titles]
        for i in top_title_indices:

            # start with the next level of elements
            parts = title_list[i].split(" ")[1:]
            parts[0] = parts[0].lower()
            new_title = "".join(parts)
            top_node = ET.SubElement(metadata,new_title)
            if elements[title_list[i]] != "":
                top_node.text=elements[title_list[i]]

            # check for multiple layers
            if len(top_title_indices) == 1:
                index = 0
                while index < len(title_list[1:]) - 1:
                    index = add_child(parent=top_node,
                                      index=index,
                                      title_list=title_list[1:],
                                      elements=elements)
            else:
                # not sure this will work but meh...
                index = 0
                for j,title in enumerate(title_list[1:i+1]):
                    while index < len(title_list[1:i+1]) - 1:
                        index = add_child(parent=top_node,
                                        index=index,
                                        title_list=title_list[1:],
                                        elements=elements)

        # write xml
        tree = ET.ElementTree(metadata)
        ET.indent(tree, space="\t", level=0)
        tree.write(self.eml_xml, encoding="utf-8", xml_declaration=True)

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

        if self.occurrences is None:
            raise ValueError("You need to have a passing, valid occurrence dataframe for this")
        
        # get dwc terms
        dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv")
        dwc_terms_rec = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
        dwc_terms_info = pd.DataFrame({'name': list(dwc_terms_rec['term_localName']), 'link': ["".join([row['version_isDefinedBy'].replace('version/',""),
                                                    row['term_localName']]) for i,row in dwc_terms_rec.iterrows()]})
        
        if len(list(set(list(self.occurrences.columns)).intersection(list(dwc_terms_info['name'])))) < self.occurrences.shape[1]:
            raise ValueError("You are still missing some DwCA Terms.")

        # initialise metadata
        metadata = ET.Element("archive")
        metadata.set('xmlns', 'http://rs.tdwg.org/dwc/text/')
        metadata.set('metadata',self.eml_xml)

        # set the core of the archive
        core = ET.SubElement(metadata,"core")
        core.set("encoding","UTF-8")
        core.set("rowType","http://rs.tdwg.org/dwc/terms/Occurrence")
        core.set("fieldsTerminatedBy",",") # CHANGE THIS TO WHATEVER OCCURRENCE IS
        core.set("linesTerminatedBy","\r\n") 
        core.set("fieldsEnclosedBy","&quot;")
        core.set("ignoreHeaderLines","1")

        # set locations of occurrence data
        core_files = ET.SubElement(core,"files")
        location = ET.SubElement(core_files,self.occurrences_name)

        # set id
        id = ET.SubElement(core,"id")
        id.set("index","0")

        # set all fields
        for i,fields in enumerate(list(self.occurrences.columns)):
            field = ET.SubElement(core,"field")
            field.set("index","{}".format(i))
            index = dwc_terms_info[dwc_terms_info['name'] == fields]['link'].index[0]
            field.set("term",dwc_terms_info[dwc_terms_info['name'] == fields]['link'][index])

        ### TODO: write capability for extensions

        # write metadata
        tree = ET.ElementTree(metadata)
        ET.indent(tree, space="\t", level=0)
        tree.write(self.meta_xml, xml_declaration=True)


# for building xml
def add_child(parent=None,
              index=None,
              title_list=None,
              elements=None):
    """
    add child to XML
    """

    # check the level of elements
    parts1 = title_list[index].split(" ")

    # first check if we are at the end of the list
    if index == len(title_list) - 1:
        new_title = create_title(title_list[index]) 
        temp = ET.SubElement(parent,new_title)
        if type(elements[title_list[index]]) is list:
            temp.text = " ".join(elements[title_list[index]])
        return index
    
    # if we are not, check the next element
    parts2 = title_list[index+1].split(" ")

    # check to see if index is still incrementing
    if index < len(title_list):

        # check to see if the next element is a child
        if len(parts1[0]) < len(parts2[0]):

            # create new subelement
            new_title = create_title(title_list[index])
            temp = ET.SubElement(parent,new_title)
            if type(elements[title_list[index]]) is list:
                temp.text = " ".join(elements[title_list[index]])
            
            # increment index
            index += 1

            # check if there are any more children 
            index = add_child(parent=temp,
                                index=index,
                                title_list=title_list,
                                elements=elements)
            
        # check to see if the elements have the same parent
        elif len(parts1[0]) == len(parts2[0]):

            # create first element
            temp = add_element(elements=elements,
                               parent=parent,
                               title_list=title_list,
                               index=index)
            
            # create second element (i+1)
            temp2 = add_element(elements=elements,
                               parent=parent,
                               title_list=title_list,
                               index=index+1)

            # check for more children (and increment index by 2)
            index = add_child(parent=parent,
                                index=index+2,
                                title_list=title_list,
                                elements=elements)
            
            # return index at the end
            return index
        
        # otherwise, next element is a new parent
        else:

            # create a new element
            temp = add_element(elements=elements,
                               parent=parent,
                               title_list=title_list,
                               index=index)
            
            # increment index and return it
            index += 1
            return index

    # return the index
    return index

def add_element(elements=None,
                parent = None,
                title_list = None,
                index=None):
    
    # create a new element
    new_title = create_title(title_list[index])
    if "citetitle" in new_title:
        temp = ET.SubElement(parent,"ulink")
        temp.set("url",elements[title_list[index]][0])
        name_licence = ET.SubElement(temp,new_title)
        name_licence.text = elements[title_list[index]][1]
    else:
        temp = ET.SubElement(parent,new_title)
    if type(elements[title_list[index]]) is list:
        temp.text = " ".join(elements[title_list[index]])
    return temp

def create_title(title=None):

    # create a title with camel case and no numbers
    parts = title.split(" ")[1:]
    parts[0] = parts[0].lower()
    new_title = "".join(parts)
    if new_title[-1].isdigit():
        new_title = new_title[:-1]
    return new_title

