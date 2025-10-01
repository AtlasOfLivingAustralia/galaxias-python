import delma

def display_metadata_as_dataframe(metadata_md='metadata.md',
                                  working_dir='./'):
    """
    Writes the ``eml.xml`` file from the metadata markdown file into your current working directory.  
    The ``eml.xml`` file is the metadata file containing things like authorship, licence, institution, 
    etc.

    Parameters
    ----------
        ``metadata_md``: ``str``
            Name of the markdown file that you want to convert to EML.  Default value is ``'metadata.md'``.
        ``working_dir``: ``str``
            Name of your working directory.  Default value is ``'./'``.
                
    Returns
    -------
        ``pandas dataframe`` denoting all the information in the metadata file
    """
    return delma.display_as_dataframe(metadata_md=metadata_md,working_dir=working_dir)