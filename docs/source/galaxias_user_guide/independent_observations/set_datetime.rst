.. _set_datetime:

set_datetime
--------------------

One of the functions you can use to check certain columns of your data is ``set_datetime()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``eventDate``: the date of your observation

It can also (optionally) can check the following:

- ``eventTime``: year of your observation
- ``year``: year of your observation
- ``month``: year of your observation
- ``day``: year of your observation

``eventDate`` and automatically converting strings
====================================================

Since we can specify the column names, we can specify the ``eventDate`` column to be ``'date'``.

.. prompt:: python

    >>> my_dwca.set_datetime(dataframe=occ,eventDate='date')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 22

We get an error here because ``set_datetime()`` requires the ``eventDate`` column to be in a ``datetime`` 
format.  This is to make sure the date is formatted correctly.  Luckily, ``set_datetime()`` has a few 
arguments that will convert dates in strings to ``datetime`` format.  

- ``string_to_datetime``: when this is set to ``True``, will convert any strings in the ``eventDate`` column to ``datetime`` objects.
- ``yearfirst``: when this is set to ``True``, ``galaxias`` (and ``pandas``) assumes your date starts with the year.
- ``dayfirst``: when this is set to ``True``, ``galaxias`` (and ``pandas``) assumes your date starts with the day.

Note when both ``yearfirst`` and ``dayfirst`` are set to ``False``, ``pandas`` assumes month is first.

.. prompt:: python

    >>> my_dwca.set_datetime(eventDate='date',
    ...                      string_to_datetime=True,
    ...                      yearfirst=False,
    ...                      dayfirst=True)
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 23

what does ``check_data`` and ``suggest_workflow`` say now? 
=============================================================

.. note::
    
    Each of the ``set_*`` functions checks your data for compliance with the 
    Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> my_dwca.check_data()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 24

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> my_dwca.suggest_workflow()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 25

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_scientific_name <set_scientific_name.html>`_

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