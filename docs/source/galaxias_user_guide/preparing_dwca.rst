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

Troubleshooting
==================

Testing Occurrences
---------------------

There will be a maximum of 3 errors that you can get when creating your DwCA using ``galaxias``.  The troubleshooting guide 
for each is linked next to it: 

- ``Your column names do not comply with the DwC standard.`` 

    This means that some (or all) of your column names do not match terms that are in the Darwin Core standard.  To learn how 
    to rename columns so they are Darwin Core-compliant, look at `Renaming Columns <preparing_data/rename_columns_to_dwca.html>`_.

- ``The values in some of your columns do not comply with the DwC standard.``

    Write this later. <LINK HERE>

- ``You need to add unique identifiers into your occurrences.``

    You need to add unique identifiers to each occurrence so they are distinct from other, similar occurrences.  To add unique 
    occurrences, go to `Adding Unique IDs <preparing_data/unique_columns.html>`_.


Testing Metadata
------------------

Something.