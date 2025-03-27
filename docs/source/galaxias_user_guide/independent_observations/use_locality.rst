.. _use_locality:

use_locality
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``use_locality()``.  
This function aims to check if you have the following:

- ``continent``: the continent of your observation
- ``country``: the country of your observation
- ``countryCode``: the country code of your observation
- ``stateProvince``: the state or province of your observation
- ``locality``: locality name of your observation

If you haven't read in our example dataset in the initial data cleaning page, 
here is an example and how to read it in:

.. prompt:: python

    >>> import galaxias
    >>> import pandas as pd
    >>> occ = pd.DataFrame(
    ...     {'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
    ...     'latitude': [-35.310, '-35.273'], 
    ...     'longitude': [149.125, 149.133], 
    ...     'date': ['14-01-2023', '15-01-2023'], 
    ...     'status': ['present', 'present']}
    ... )
    >>> my_dwca = galaxias.dwca(occurrences=occ)

If you wish to follow with your own dataset in a csv file, use ``pandas`` to read 
in your csv file:

.. prompt:: python

    >>> import pandas as pd
    >>> my_dwca = galaxias.dwca(occurrences='<YOUR-FILENAME>.csv')

specifying ``continent`` and ``country``
--------------------------------------------

.. prompt:: python

    >>> my_dwca.use_locality(continent='Australia')

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 29

However, for Darwin Core purposes, ``Australia`` is a country, and ``Oceania`` is the 
continent that Australia is part of.  Therefore, we can set ``continent='Oceania'`` and 
``country='Australia'``.

.. prompt:: python

    >>> my_dwca.use_locality(continent='Oceania',country='Australia')

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 30

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `use_occurrences <use_occurrences.html>`_
- `use_coordinates <use_coordinates.html>`_
- `use_datetime <use_datetime.html>`_
- `use_scientific_name <use_scientific_name.html>`_

Optional functions:

- `use_abundance <use_abundance.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_