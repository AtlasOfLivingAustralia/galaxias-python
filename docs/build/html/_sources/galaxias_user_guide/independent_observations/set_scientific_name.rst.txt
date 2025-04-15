.. _set_scientific_name:

set_scientific_name
--------------------

One of the functions you can use to check certain columns of your data is ``set_scientific_name()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``scientificName``: the scientific name of the species you observed

It can also can check the following:

- ``scientificNameRank`` (OPTIONAL): rank of the scientific name you are providing.
- ``scientificNameAuthorship`` (OPTIONAL): Authors of the species name you are using.

specifying ``scientificName``
---------------------------------------

Like with other ``set_*`` functions, to specify which column you want to rename or change, you 
specify it with the Darwin Core term.  In this case, it is ``scientificName``.

.. prompt:: python

    >>> my_dwca.set_scientific_name(dataframe=occ,scientificName='Species')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 11

what does ``check_data`` and ``suggest_workflow`` say now? 
------------------------------------------------------------------

*Note:* each of the ``set_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> my_dwca.set_scientific_name(dataframe=occ,scientificName='Species')
    >>> my_dwca.check_dataset()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 12

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> my_dwca.suggest_workflow()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 13

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_
- `set_collection <set_collection.html>`_
- `set_individual_traits <set_individual_traits.html>`_
- `set_license <set_license.html>`_
- `set_locality <set_locality.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_