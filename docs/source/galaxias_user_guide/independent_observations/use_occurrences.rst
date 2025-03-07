.. _use_occurrences:

use_occurrences
--------------------

One of the functions you can use to check certain columns of your data is ``use_occurrences()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``basisOfRecord``: how the occurrence was recorded (was it observed by a human? machine? is it part of a collection?)
- ``occurrenceID`` or ``catalogNumber`` or ``recordNumber``: a unique identifier for the record (only one of these is necessary)
- ``occurrenceStatus`` (OPTIONAL): whether a species is present or absent.  Not required for data submission.

Initial run of ``use_occurrences``
---------------------------------------

Initally, let's run ``use_occurrences()`` to see if any of our columns match the Darwin 
Core Vocabulary mentioned above:

.. prompt:: python

    >>> my_archive.use_occurrences()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 3

Here, we can see that we don't have any column names matching ``basisOfRecord``, ``occurrenceStatus``, 
``occurrenceID``, ``catalogNumber`` or ``recordNumber``.  Luckily, there are options in ``use_occurrences()`` 
that allow the user to specify a column of data as one of the column names, or to set a default value for 
the column.

Specifying ``basisOfRecord`` value
---------------------------------------

As mentioned above, the ``basisOfRecord`` value is a required and important 
field for an observation, as it lets others know how the record was recorded.  
For example, was it a machine that observed it? A human? Is this a specimen 
that's part of a collection?

Depending on your answer to these questions, the information you provide will differ.  
Luckily, Darwin Core has a predefined vocabulary to help you with this.  The current 
accepted values are as follows:

.. program-output:: python galaxias_user_guide/independent_observations/bor_values.py

For this exercise, let's assume a human has seen these, which equates to a value of 
``HumanObservation``.  We can then set the ``basisOfRecord`` argument as ``HumanObservation``, 
and it will, by default, set the value of ``basisOfRecord`` for the whole dataframe.

.. prompt:: python

    >>> my_archive.use_occurrences(
    ...     basisOfRecord='HumanObservation'
    ... )
    >>> my_archive.occurrences.head()    

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 5

How to generate occurrence IDs 
---------------------------------------

*Note:* If you have occurrence IDs already in your dataset, you can specify the name of the column 
that contains your IDs, and ``galaxias`` will rename that column to comply with the Darwin Core Vocabulary 
Standard.

*Note:* ``catalogNumber`` and / or ``recordNumber`` is normally used for collections, 
so it is best to go with ``occurrenceID`` if you're generating them using ``galaxias``.

Every occurrence needs a unique identifier for easy future identification.  If your 
occurences don't have either an ``occurrenceID``, ``catalogNumber`` or ``recordNumber``, 
you can provide a value of ``True`` to the ``occurrenceID``, and unique identifiers 
will be generated for you.

.. prompt:: python

    >>> my_archive.use_occurrences(
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceID=True
    ... )
    >>> my_archive.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 6

specify ``occurrenceStatus`` column
---------------------------------------

*Note:* This is an optional field, but we are including it here to share how this argument works, and how this will rename your column

Sometimes, you may want to include the ``occurrenceStatus`` field in your observations, especially 
if you were expecting to see a species in a particular area, and/or have seen them in the past but 
did not see them on that particular day, you can include this to say they were absent.

Since we have a column that denotes whether or not a species was present or absent, we can 
provide the name of that column, and ``galaxias`` will rename the column to conform with the 
Darwin Core standard.

.. prompt:: python

    >>> my_archive.use_occurrences(
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='PRESENT'
    ... )
    >>> my_archive.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 7

what does ``check_data`` and ``suggest_workflow`` say now? 
-------------------------------------------------------------

*Note:* each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now that we've taken care of the pieces of information ``use_occurrences()`` is responsible 
for, we can assign the new dataframe to a variable:

.. prompt:: python

    >>> occ = my_archive.use_occurrences(
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='status',
    ...     occurrenceID=True
    ... )

Now, we can check that this new dataframe complies with the Darwin Core standard for the ``basisOfRecord``, 
``occurrenceStatus``, ``occurrenceID``, ``catalogNumber`` and ``recordNumber`` columns.

.. prompt:: python

    >>> my_archive.check_dataset()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 8

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see what other functions we can use to check our data:

.. prompt:: python

    >>> my_archive.suggest_workflow()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 9

Other functions
---------------------------------------

To learn more about how to use these functions, go to 

- `use_coordinates <use_coordinates.html>`_
- `use_datetime <use_datetime.html>`_
- `use_scientific_name <use_scientific_name.html>`_

Optional functions:

- `use_abundance <use_abundance.html>`_
- `use_locality <use_locality.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_