.. _set_abundance:

set_abundance
--------------------

.. Note:: 
    
    Abundance information is not required by the ALA, but it is nice to have.

One of the functions you can use to check your data is ``set_abundance()``.  
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

You can also specify the  number of individuals you observed with the ``individualCount`` 
argument.

.. prompt:: python

    >>> my_dwca.set_abundance(dataframe=occ,individualCount='count')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 27

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_collection <set_collection.html>`_
- `set_individual_traits <set_individual_traits.html>`_
- `set_license <set_license.html>`_
- `set_locality <set_locality.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_