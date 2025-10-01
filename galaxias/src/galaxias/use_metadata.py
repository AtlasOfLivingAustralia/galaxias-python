import delma

def use_metadata(metadata_md='metadata.md',
                 working_dir='./',
                 publishing_dir='./data-publish',
                 eml_xml='eml.xml'):
    """
    Writes the metadata file into an ``xml`` format in your publishing directory
    
    Parameters
    ----------
        ``metadata_md``: ``str``
            Name of the markdown file that you want to convert to EML.  Default value is ``'metadata.md'``.
        ``working_dir``: ``str``
            Name of your working directory.  Default value is ``'./'``.
        ``publishing_dir``: ``str``
            Name of the directory containing your data for publication.  Default value is ``'./'``.
        ``eml_xml``: ``str``
            Name of your eml xml file.  Default value is ``'eml.xml'``.
                
    Returns
    -------
        ``None``
    """
    delma.write_eml(metadata_md=metadata_md,working_dir=working_dir,publishing_dir=publishing_dir,
                    eml_xml=eml_xml)