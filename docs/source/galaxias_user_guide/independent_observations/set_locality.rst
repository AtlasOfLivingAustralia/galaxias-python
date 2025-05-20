.. _set_locality:

set_locality
--------------------

.. Note:: 
    
    Locality information is not required by the ALA, but it is nice to have.

One of the functions you can use to check your data is ``set_locality()``.  
This function aims to check if you have the following:

- ``continent``: the continent of your observation
- ``country``: the country of your observation
- ``countryCode``: the country code of your observation
- ``stateProvince``: the state or province of your observation
- ``locality``: locality name of your observation

specifying ``continent`` and ``country``
--------------------------------------------

.. prompt:: python

    >>> my_dwca.set_locality(continent='Australia')

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 29

However, for Darwin Core purposes, ``Australia`` is a country, and ``Oceania`` is the 
continent that Australia is part of.  Therefore, we can set ``continent='Oceania'`` and 
``country='Australia'``.

.. prompt:: python

    >>> my_dwca.set_locality(continent='Oceania',country='Australia')

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 30

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_
- `set_collection <set_collection.html>`_
- `set_individual_traits <set_individual_traits.html>`_
- `set_license <set_license.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_