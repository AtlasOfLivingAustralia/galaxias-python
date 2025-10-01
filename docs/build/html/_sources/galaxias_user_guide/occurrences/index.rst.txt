:orphan:

Standardising an Occurrence Dataset
===================================

*Amanda Buyan, Dax Kellie & Martin Westgate*

In Living Atlases like the Atlas of Living Australia (ALA), the default type of data is 
*occurrence* data, where a record refers to the presence/absence of an organism or taxon 
in a particular place at a specific time. This is a relatively simple data structure, where 
it is assumed that each observation or record is independent of each other. This simplicity 
also allows occurrence-based data to be easily aggregated. 

Here, we'll go through the steps to standardise and build an occurrence dataset using ``galaxias``. 

The dataset
--------------------------------------------------

:download:`Example Occurrences<../data/dummy-dataset-sb.csv>`

The data we'll use are of bird observations from 4 different sites. As these are *occurrence* data, 
this dataset contains evidence of the presence of certain bird species (``species``) at particular 
locations (``lat``, ``lon``) at specific times (``date``). It also contains additional information 
about the landscape type, and sex and age class of birds.  

.. prompt:: Python

    >>> import galaxias
    >>> occurrences = pd.read_csv('dummy-dataset-sb.csv')
    >>> # set all titles to lowercase
    >>> occurrences.columns = map(str.lower, occurrences.columns)
    >>> occurrences

.. program-output:: python galaxias_user_guide/occurrences/data_cleaning.py 1

Standardise to Darwin Core
--------------------------------------------------

We can use ``suggest_workflow()`` to determine what we need to do to standardise this dataset. 

.. prompt:: Python

    >>> galaxias.suggest_workflow(occurrences=occurrences)

.. program-output:: python galaxias_user_guide/occurrences/data_cleaning.py 2

Calling ``suggest_workflow()`` tells us that one column in the dataset matches Darwin Core 
terms (``sex``), and we are missing all the minimum required Darwin Core terms. We're also 
given a suggested workflow consisting of a series of ``set_`` functions for renaming, 
modifying, or adding missing columns. ``set_`` functions are specialised wrappers around the 
``{pandas}`` package, with additional functionality to support using Darwin Core Standard.

Let's start by renaming existing columns to align with Darwin Core terms. ``set_`` functions 
will automatically check to make sure each column is correctly formatted.

.. prompt:: Python

    >>> occurrences = galaxias.set_scientific_name(scientificName = 'species')
    >>> occurrences = galaxias.set_coordinates(decimalLatitude = 'lat',
    ...                                        decimalLongitude = 'lon')
    >>> occurrences = galaxias.set_datetime(eventDate = 'date',
    ...                                     string_to_datetime=True,
    ...                                     yearfirst = True)

Calling `suggest_workflow()` again accounts for our progress and shows us what still needs to be done. 
Here, we can see that we're still missing a couple of minimum required terms. 

.. prompt:: Python

    >>> galaxias.suggest_workflow(occurrences=occurrences)

.. program-output:: python galaxias_user_guide/occurrences/data_cleaning.py 3

Here’s a rundown of the columns we need to add:

- ``occurrenceID``: Unique identifier for each record, which ensures that we can identify specific records for future updates or corrections. We can use `composite_id()`, `sequential_id()`, or `random_id()` to add a unique ID to each row.
- ``basisOfRecord``: The type of record (e.g. human observation, specimen from a museum collection, machine observation). See a list of acceptable values with `corella::basisOfRecord_values()`.
- ``geodeticDatum``: The geographic coordinate reference system (CRS), which is a framework for representing spatial data (for example, the CRS of Google Maps is "WGS84").
- ``coordinateUncertaintyInMeters``: The area of uncertainty around your observation, which you may be able to infer based on your data collection method.

As suggested, let’s add these columns using ``set_occurrences()`` and ``set_coordinates()``. We 
can also use an optional function, ``set_individual_traits()``, which will automatically 
identify the matched column name ``sex`` and check the column’s format.

.. dropdown:: Creating unique ``occurrenceID`` 
    :color: info
    
    There are multiple ways of creating unique IDs for your occurrences.  For creating either 
    sequential or random IDs, you only have to provide the keywords ``sequential`` or ``random``.

    To create a unique ID using column names, simply provide the column names in a list to the 
    ``occurrenceID`` argument, and 

    .. prompt:: Python

        >>> #example code snippet of having a sequential ID first
        >>> occurrences = galaxias.set_occurrences(occurrences=occurrences,occurrenceID = ['sequential','site','landscape'])
        >>> 
        >>> #example code snippet of having a random ID last
        >>> occurrences = galaxias.set_occurrences(occurrences=occurrences,occurrenceID = ['site','landscape','random'])

.. prompt:: Python

    >>> occurrences = galaxias.set_occurrences(occurrences=occurrences,occurrenceID = ['sequential','site','landscape'],
    ...                                        basisOfRecord = 'HumanObservation')
    >>> occurrences = galaxias.set_coordinates(dataframe=occurrences,geodeticDatum = 'WGS84',
    ...                                         coordinateUncertaintyInMeters = 30)
    >>> occurrences = galaxias.set_individual_traits(dataframe=occurrences)

.. dropdown:: What if my lat/long are in degrees, minutes, seconds? 
    :color: info
    
    The Atlas of Living Australia requires that lat/longs be in decimal degrees.  
    If your lat/longs are in degrees, minutes and seconds (DMS), there is a Python package 
    that will convert your lat/longs into decimal degrees: `lat_lon_parser <https://github.com/NOAA-ORR-ERD/lat_lon_parser>`_.  

    Below is a code snippet used on an example dataframe to convert from DMS to 
    decimal degrees.  To do this on an ``occurrences`` dataframe in a ``dwca`` 
    object, replace the variable ``occ`` with ``<NAME_OF_DWCA_OBJECT>.occurrences``.

    .. prompt:: python

        >>> from lat_lon_parser import parse
        >>> import pandas as pd 
        >>> occ = pd.DataFrame(
        ...     {
        ...         'decimalLatitude': ["35\° 50' 11\"", "45\° 51' 13\"", "30\° 20' 10\""], 
        ...         'decimalLongitude': ["138\° 01\' 26\"", "139\° 11\' 16\"", "128\° 05\' 29\""]
        ...     }
        ... )
        >>> for i, row in occ.iterrows():
        ...     occ.at[i, 'decimalLatitude'] = round(parse(row['decimalLatitude']),2)
        ...     occ.at[i, 'decimalLongitude'] = round(parse(row['decimalLongitude']),2)
        >>> occ

    .. program-output:: python galaxias_user_guide/occurrences/convert_coords.py

Running ``suggest_workflow()`` once more confirms that our dataset has all the required 
information to be put into a Darwin Core Archive!

.. prompt:: Python

    >>> galaxias.suggest_workflow(occurrences=occurrences)

.. program-output:: python galaxias_user_guide/occurrences/data_cleaning.py 4

Here, you can do one of two things:

1. Select only the columns which are currently Darwin core compliant
2. Use optional functions to ensure other parts of your data are Darwin core compliant, and include those in your final dataset.

To see which Darwin core terms are included in checks in ``galaxias``, consult the list below.

.. dropdown:: Supported Darwin Core Terms and Their Associated Functions 
    :color: info
    
    .. csv-table:: 
        :file: ../data/supported-terms.csv
        :widths: 20, 40  
        :header-rows: 1

To select only the columns that are Darwin core compliant, run the following snippet of code:

.. prompt:: Python

    >>> occ_terms = list(galaxias.occurrence_terms())
    >>> occ_terms_dwca = list(set(occ_terms).intersection(list(occurrences.columns)))
    >>> occurrences_final = occurrences[occ_terms_dwca]
    >>> occurrences_final

.. program-output:: python galaxias_user_guide/occurrences/data_cleaning.py 5

We can specify that we wish to use occurrences and events in our Darwin Core Archive 
with ``use_data()``, which will save your occurrences as individual ``csv`` 
files in the default directory ``data-publish`` as ``occurrences.csv``.

.. prompt:: Python

    >>> galaxias.use_data(occurrences=occurrences_final)

In data terms, that’s it! Don’t forget to add metadata.  An explanation of how to add metadata
is `here <../creating_your_metadata.html>`_.