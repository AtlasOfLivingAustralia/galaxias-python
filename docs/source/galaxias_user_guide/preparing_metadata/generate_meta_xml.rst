:orphan:

Making Your Descriptor File
===============================

Have you done this?

.. prompt:: python

    >>> import galaxias
    >>> data = pd.read_csv("data_clean.csv")
    >>> my_dwca = galaxias.dwca(occurrences=data)
    >>> my_dwca.make_eml_xml()

Now, do this.

.. prompt:: python

    >>> my_dwca.make_meta_xml()

.. program-output:: python galaxias_user_guide/preparing_metadata_script.py meta