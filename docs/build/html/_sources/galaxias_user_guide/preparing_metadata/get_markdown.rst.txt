:orphan:

Getting A Markdown File
===============================

Thankfully, ``galaxias`` creates a metadata file when you create the ``dwca`` object.  By default, it will 
be named ``metadata.md``, and exist in your current working directory.

.. program-output:: ls ../metadata.md

To change the metadata file to something you already have, you have to provide the filename to the ``metadata_md`` 
argument during the initial creation of the ``dwca`` object.

.. prompt:: python

    >>> import galaxias
    >>> data = pd.read_csv("data_clean.csv")
    >>> my_dwca = galaxias.dwca(occurrences=data,metadata_md=<NAME_OF_FILE_HERE>)