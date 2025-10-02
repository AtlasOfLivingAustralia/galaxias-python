import delma

def use_metadata_template(metadata_md='metadata.md',
                          working_dir='./',
                          xml_url=None,
                          print_notices=False):
    """
    This function is for creating a metadata statement, either from a bulk

    Parameters
    ----------
        ``metadata_md`` : ``str``
            Name of the metadata file you will edit.  Default is ``'metadata.md'``.
        ``working_dir``: ``str``
            Name of your working directory.  Default value is ``'./'``.
        ``xml_url`` : ``str``
            URL of the eml xml file you want to emulate.  Default is ``None``.  

    Returns
    -------
        ``None``
    """
    delma.create_md(metadata_md=metadata_md,working_dir=working_dir,
                    xml_url=xml_url,print_notices=print_notices)