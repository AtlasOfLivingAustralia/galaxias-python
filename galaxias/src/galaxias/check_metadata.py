import delma

def check_metadata(eml_xml='eml.xml',
                   eml_dir='./data-publish'):
    """
    Checks whether or not your eml xml file is formatted correctly for GBIF.

    Parameters
    ----------
        ``eml_xml``: ``str``
            Name of the eml xml file you want to validate.  Default value is ``'eml.xml'``.
        ``eml_dir``: ``str``
            Name of the directory to write the ``eml.xml``.  Default value is ``'./'``.

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns None if it passes.
    """
    delma.check_metadata(eml_dir=eml_dir,eml_xml=eml_xml)