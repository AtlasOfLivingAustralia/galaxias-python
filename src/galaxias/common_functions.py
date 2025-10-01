import os
import pandas as pd
import xml.etree.ElementTree as ET

def snake_to_camel_case(list_of_words=None):

    new_list = []
    for w in list_of_words:
        term = w.lower().split("_")
        for i in range(len(term)):
            term[i] = term[i].capitalize()
        new_list.append("".join(term))
    return new_list

def write_to_zip_and_disk(zf=None,
                          copyfile=None,
                          removefile=None):

    os.system("cp {} .".format(copyfile))
    zf.write(removefile)
    os.system("rm {}".format(removefile))

def add_file_to_dwca(zf=None,
                     dataframe=None,
                     publishing_dir=None,
                     file_to_write=None):
    
    # check if your data file has been written
    if not os.path.exists("{}".format(file_to_write)):
        dataframe.to_csv("{}".format(file_to_write),index=False)

    # first, write occurrences to zip and disk
    zf.write("{}/{}".format(publishing_dir,file_to_write))

def read_dwc_terms_links():
    '''Reads in accepted DwC terms from the given link to a csv'''

    # dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv")
    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv") # version_status
    dwc_terms_rec = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    dwc_terms_info = pd.DataFrame({'name': list(dwc_terms_rec['term_localName']), 'link': ["".join([row['version_isDefinedBy'].replace('version/',""),
                                                row['term_localName']]) for i,row in dwc_terms_rec.iterrows()]})
    dwc_terms_info = pd.concat([dwc_terms_info,pd.DataFrame({'name': 'identifier', 'link': 'http://rs.tdwg.org/dwc/terms/version/identifier'},index=[0])]).reset_index(drop=True) # temporary until we fix stuff with multimedia
    return dwc_terms_info

def read_dwc_terms_list():
    '''Reads in accepted DwC terms from the given link to a csv'''

    # dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv")
    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv")
    dwc_terms_recommended = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    list_terms_recommended = list(dwc_terms_recommended["term_localName"]) + ['identifier'] # temporary until we fix stuff with multimedia
    return list_terms_recommended

def build_subelement(element=None,
                     row_type=None,
                     filename=None,
                     data=None,
                     dwc_terms_info=None):
    """
    Builds a subelement of the eml.xml tree.

    Parameters
    ----------
        ``element``: ``xml ElementTree subelement`` 
            Option whether to return a dictionary object containing full taxonomic information on your species.  Default to ``False``. 
        ``path`` : ``str``
            File path to your working directory.  Default is directory you are currently in.
    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.

    Examples
    --------
    Amanda to add here later.

    """

    # set all basic elemnt things
    element.set("rowType",row_type)
    element.set("encoding","UTF-8")
    element.set("fieldsTerminatedBy",",") # CHANGE THIS TO WHATEVER OCCURRENCE IS
    element.set("linesTerminatedBy","\\r\\n") 
    element.set("fieldsEnclosedBy","&quot;")
    element.set("ignoreHeaderLines","1")

    # set locations of occurrence data
    element_files = ET.SubElement(element,"files")
    location = ET.SubElement(element_files,"location")
    location.text = filename

    # set id
    if element.tag == 'core':
        id = ET.SubElement(element,"id")
        id.set("index","0")
    elif element.tag == 'extension':
        id = ET.SubElement(element,"coreid")
        id.set("index","0")
    else:
        raise ValueError("Elements can only be core or extension.  You have {}".format(element.tag))

    # set all fields
    for i,fields in enumerate(list(data.columns)):
        field = ET.SubElement(element,"field")
        field.set("index","{}".format(i)) # added a plus one
        index = dwc_terms_info[dwc_terms_info['name'] == fields]['link'].index[0]
        field.set("term",dwc_terms_info[dwc_terms_info['name'] == fields]['link'][index])

    # return element
    return element