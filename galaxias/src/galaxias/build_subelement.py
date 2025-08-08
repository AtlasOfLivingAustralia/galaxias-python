import xml.etree.ElementTree as ET

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
