.. _Quick_Start_Guide:

Quick Start Guide
=======================

galaxias is a Python package that helps users bundle their data into a standardised format 
optimised for storing, documenting, and sharing biodiversity data. This standardised format 
is called a `Darwin Core Archive <https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide#what-is-darwin-core-archive-dwc-a>`_ — 
a zip file containing data and metadata that conform to the Darwin Core Standard, the accepted data standard of the Global Biodiversity Information Facility (GBIF) and its partner nodes (e.g. the Atlas of Living Australia).

Sharing Darwin Core Archives with data infrastructures allows data to be reconstructed and aggregated accurately. Let’s see how to prepare a Darwin Core Archive using galaxias.

Getting Started
--------------------------------------

Here we have an existing folder structure containing data collected over the course of a research project. Our project uses a fairly standard folder structure.

.. prompt:: Python

    ├── README.md                        : Description of the repository
    ├── data                             : Folder to store cleaned data
    |  └── my_data.csv
    ├── data-raw                         : Folder to store original/source data
    |  └── my_raw_data.csv
    ├── plots                            : Folder containing plots/dataviz
    └── scripts                          : Folder with analytic coding scripts

Let’s see how galaxias can help us to package our data as a Darwin Core Archive.

Use standardised data in an archive
--------------------------------------

Data that we wish to share are in the data folder. When the data is read into Python, 
they might look something like this:

.. prompt:: Python

    >>> import pandas as pd
    >>> my_data = pd.read_csv('data/my_data.csv')
    >>> my_data

.. program-output:: python getting_started/getting_started_code.py 1

First, we’ll need to standardise our data to conform to the Darwin Core Standard. suggest_workflow() can help by summarising our dataset and suggesting the steps we should take.

.. prompt:: Python

    >>> galaxias.suggest_workflow(occurrences=my_data)

.. program-output:: python getting_started/getting_started_code.py 2

Following the advice of suggest_workflow(), we can use the ``set_`` functions to standardise 
the ``my_dwca`` occurrences data. ``set_`` functions work a lot like extant functions in ``pandas``: 
they modify existing columns or create new columns. The suffix of each ``set_`` function 
gives an indication of the type of data it accepts (e.g. ``set_coordinates()``, 
``set_scientific_name``), and function arguments are valid Darwin Core terms to use as 
column names. Each ``set_`` function also checks to make sure that each column contains 
valid data according to Darwin Core Standard.

.. prompt:: Python

        >>> # basic requirements of Darwin Core
        >>> my_data = galaxias.set_occurrences(occurrences=my_data,
        ...                                    occurrenceID = 'sequential',
        ...                                    basisOfRecord = 'HumanObservation')
        >>> # place and time
        >>> my_data = galaxias.set_coordinates(dataframe=my_data,
        ...                                    decimalLatitude = 'latitude', 
        ...                                    decimalLongitude = 'longitude')
        >>> my_data = galaxias.set_locality(dataframe=my_data,
        ...                                 country = "Australia", 
        ...                                 locality = "Canberra")
        >>> my_data = galaxias.set_datetime(dataframe=my_data,
        ...                                 eventDate = 'date',
        ...                                 eventTime = 'time',
        ...                                 string_to_datetime=True,
        ...                                 dayfirst=True,
        ...                                 yearfirst=False,
        ...                                 time_format='mixed')
        >>> # taxonomy
        >>> my_data = galaxias.set_scientific_name(dataframe=my_data,
        ...                                        scientificName = 'species', 
        ...                                        taxonRank = 'species')
        >>> my_data = galaxias.set_taxonomy(dataframe=my_data,
        ...                                 kingdom = 'Animalia',
        ...                                 family = 'Cacatuidae') 

.. program-output:: python getting_started/getting_started_code.py 3

You may have noticed that we added some additional columns that were not included in the 
advice of ``suggest_workflow()`` (``country``, ``locality``, ``taxonRank``, ``kingdom``, 
``family``). We encourage users to specify additional information where possible to avoid 
ambiguity once their data are shared.

To use our standardised data in a Darwin Core Archive, we can select columns that use 
valid Darwin Core terms as column names. Invalid columns won’t be accepted when we try 
to build our Darwin Core Archive. Our data is an occurrence-based dataset (each row 
contains information at the observation level, as opposed to site/survey level), so 
we’ll select columns that match names in ``occurrence_terms()``.

.. prompt:: Python

    >>> occ_terms = list(galaxias.occurrence_terms())
    >>> occ_terms_dwca = list(set(occ_terms).intersection(list(my_data.columns)))
    >>> my_data_final = my_data[occ_terms_dwca]
    >>> my_data_final

.. program-output:: python getting_started/getting_started_code.py 4

Add metadata
--------------------------------------

A critical part of a Darwin Core archive is a metadata statement: this tells users who 
owns the data, what the data were collected for, and what uses they can be put to 
(i.e. a data licence). A boilerplate metadata statement is made when you create your 
``dwca`` object.  By default, this creates a markdown template named metadata.md in 
your working directory.  We can edit this template to include information about our 
dataset, and write the metadata to disk using ``write_eml()``.

.. prompt:: Python

    >>> galaxias.use_metadata_template()
    >>> galaxias.use_metadata()

This converts our metadata statement to Ecological Meta Language (EML), the accepted 
format of metadata for Darwin Core Archives, and saves it as ``eml.xml`` in the 
``data-publish`` folder.

Build an archive
--------------------------------------

At the end of the above process, we should have a folder named ``data-publish`` 
that contains at least one file, and potentially two:

- An eml.xml file containing your metadata 
- One or more ``.csv`` files containing data (e.g. ``occurrences.csv``, ``events.csv``, ``multimedia.csv``)

We can now run ``build_archive()`` to build our Darwin Core Archive!

.. prompt:: Python
    
    >>> galaxias.build_archive()

Running ``build_archive()`` will go through the following steps:

- Writes all the processed data into ``csv`` files
- Checks whether we have completed the ``eml.xml`` file
- Checks whether we have a ‘schema’ document (meta.xml) in our ``data-publish`` folder
- Puts all required files into a darwin core archive

.. dropdown:: Schema (``meta.xml``) 
    :color: primary
    
    This is a machine-readable xml document that describes the content of the archive’s 
    data files and their structure. The schema document is a required file in a Darwin 
    Core Archive. If it is missing, ``build_archive()`` will build one. We can also 
    build a schema document ourselves using ``make_meta_xml()``.

At the end of this process, you should have a Darwin Core Archive zip file (``dwca.zip``) 
in your parent directory. You should also have a ``data-publish`` folder in your working 
directory containing standardised data files (e.g. ``occurrences.csv``), a metadata 
statement in EML format (``eml.xml``), and a schema document (``meta.xml``).

Check archive
--------------------------------------

There are two ways to check whether the contents of your Darwin Core Archive meet the 
Darwin Core Standard.

The first is to run local tests on the files inside a local folder directory that will 
be used to build a Darwin Core Archive. ``check_directory()`` allows us to check csv 
files and xml files in the directory against Darwin Core Standard criteria, using the 
same checking functionality that is built into the ``set_`` functions. This function 
is especially beneficial if you have standardized your data to Darwin Core headers 
using functions outside of ``galaxias`` / ``corella``.

.. prompt:: Python

    >>> galaxias.check_directory()

The second is to check whether a complete Darwin Core Archive meets institution’s 
Darwin Core criteria via an API. For example, we can test an archive against GBIF’s API 
tests.  This is not currently recommended, however, as 

.. prompt:: Python

    >>> # Check against GBIF API
    >>> galaxias.check_archive("dwc-archive.zip",
    ...                        email = "your-email",
    ...                        username = "your-username",
    ...                        password = "your-password")

Publish/share your archive
--------------------------------------
The final step is to share your completed Darwin Core Archive with a data infrastructure 
like the Atlas of Living Australia. To share with the ALA, you can launch our data 
submission process in your browser by calling:

.. prompt:: Python

    >>> galaxias.submit_archive()

This function will provide you with the option to open a GitHub issue where you can 
attach your archive. We will run the galaxias test suite on your dataset and respond 
as soon as we can.

If you’d prefer not to use GitHub, you can send your file and a brief description to 
`support@ala.org.au <mailto:support@ala.org.au>`_.