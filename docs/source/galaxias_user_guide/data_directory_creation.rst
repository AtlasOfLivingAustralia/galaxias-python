:orphan:

Reading and Storing Your Data on Disk
=======================================

So we are adhering to best practices for data cleaning, we have included the automatic 
creation of a folder on your local computer whereby an original copy of your data is stored, 
along with a copy of your "Darwin-Core Compliant" data (i.e. data you have changed).

Default
--------------------------------

If you want to go with the default options for where your data is stored, you 
simply create a ``dwca`` object, and ``galaxias`` will create a folder called ``dwca_data``.

.. prompt:: Python

    >>> import galaxias
    >>> my_dwca = galaxias.dwca(occurrences="occurrences.csv")

If you look inside this folder, it will have two subfolders and one markdown file:

- ``raw_data/``
- ``processed_data/``
- ``metadata.md``

The first directory, titled ``raw_data``, is where your original data is kept.  This 
is so in case mistakes are made, or you want to preserve the raw data alongside your 
cleaned data, you can do so.

The second directory, titled ``processed_data``, is where all your processed data 
files will be written when you are ready to put the data into your DwCA.

The last file, titled ``metadata.md``, is a markdown template of all the fields 
you may want to include in your metadata.

Custom Names
--------------------------------

If you prefer to have your own names for each folder, you can provide them as arguments 
during your initial Darwin Core Archive, as per the code below:

.. prompt:: Python

    >>> import galaxias
    >>> my_dwca = galaxias.dwca(occurrences="occurrences.csv",
                                working_dir = <NAME_OF_FOLDER>,
                                data_raw_dir = <NAME_OF_FOLDER>,
                                data_proc_dir = <NAME_OF_FOLDER>)

The first argument, ``working_dir``, is where all of your data will be stored.  ``data_raw_dir`` is the 
name of the folder where you will keep an original copy of your data.  ``data_proc_dir`` is where you 
will keep the data you clean.

Next: `Generate An Initial Report <initial_report.html>`_.