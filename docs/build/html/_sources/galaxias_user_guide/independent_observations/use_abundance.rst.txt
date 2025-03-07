.. _use_abundance:

use_abundance
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``use_abundance()``.  
This function aims to check that you have the following:

- ``individualCount``: the number of individuals observed of a particular species

It can also (optionally) can check the following:

- ``organismQuantity``: a description of your individual counts
- ``organismQuantityType``: describes what your organismQuantity is

For this exercise, we have included an extra column from the example dataframe titled ``'count'``:

.. prompt:: python

    >>> import galaxias
    >>> import pandas as pd
    >>> occ = pd.DataFrame(
    ...     {'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
    ...     'latitude': [-35.310, '-35.273'], 
    ...     'longitude': [149.125, 149.133], 
    ...     'date': ['14-01-2023', '15-01-2023'], 
    ...     'status': ['present', 'present'],
    ...     'count': [2,1]}
    ... )
    >>> my_dwca = my_dwca.dwca(occurrences=occ)

If you wish to follow with your own dataset in a csv file, use ``pandas`` to read 
in your csv file:

.. prompt:: python

    >>> import pandas as pd
    >>> my_dwca = my_dwca.dwca(occurrences='<FILENAME>.csv')

specifying ``individualCount``
-----------------------------------------

.. prompt:: python

    >>> my_dwca.use_abundance(dataframe=occ,individualCount='count')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 27

To learn more about how to use other functions, go to 

- `use_occurrences <use_occurrences.html>`_
- `use_coordinates <use_coordinates.html>`_
- `use_datetime <use_datetime.html>`_
- `use_scientific_name <use_scientific_name.html>`_

Optional functions:

- `use_locality <use_locality.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_