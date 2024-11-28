:orphan:

Preparing the DwCA itself 
==========================

*Note: this workflow assumes that your data will pass all checks.  If it doesn't, see the Troubleshooting 
guide below*

Preparing your Darwin Core Archive is straightforward.  For a simple occurrences DwCA, the process 
looks like this from start to finish:

.. prompt:: Python

    >>> import galaxias
    >>> my_dwca = galaxias.dwca(occurrences="occurrences.csv")
    >>> ### edit metadata.md
    >>> my_dwca.make_eml_xml()
    >>> my_dwca.make_meta_xml()
    >>> my_dwca.create_dwca()

This will produce a Darwin Core Archive titled ``dwca.zip``, which contains the files ``occurrences.csv``, 
``eml.xml`` and ``meta.xml``.  