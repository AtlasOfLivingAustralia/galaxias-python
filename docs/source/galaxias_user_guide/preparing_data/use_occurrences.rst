:orphan:

Adding Occurrence-Specific Terms
=======================================

There are two items that are specific to occurrence records that need to be included:

- At least one identifier, titled ``occurrenceID`` or ``catalogNumber`` or ``recordNumber``
- A value called ``basisOfRecord``

The identifier ensures that each of your occurrence observations are unique, while ``basisOfRecord`` 
refers to how the occurrence was recorded.  This is important for distinguishing individuals 
observed in the wild versus a museum specimen.  This can also include things like camera traps and fossils.  
Here, we show (from the ``galah-python`` package) what options are available:

.. program-output:: python -W ignore galaxias_user_guide/bor_values.py

Adding Unique Identifiers To Your Dataset
----------------------------------------------

If you don't have any unique identifiers in your dataset, and want ``galaxias`` to generate ones for you, 
use the ``use_occurrences`` function:

.. prompt:: Python

    >>> occ_dwca.use_occurrences(occurrenceID = True)
    >>> occ_dwca.occurrences.head()

Your data will then look like this:

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 2

Specifying A Value for ``basisOfRecord``
----------------------------------------------

If you don't have a ``basisOfRecord`` column in your dataset, you can use ``galaxias`` to add this column by 
including the ``basisOfRecord`` argument when you run ``use_occurrences()``:

.. prompt:: Python

    >>> occ_dwca.use_occurrences(basisOfRecord = "HumanObservation")

Your data will then look like this:

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 3

Specifying columns for identifiers and ``basisOfRecord``
---------------------------------------------------------

If your data already has these columns, but they do not have the required titles, you can instead specify a column 
of your data, and ``galaxias`` will rename it for you.

.. prompt:: Python

    >>> occ_dwca.use_occurrences(basisOfRecord = occ_dwca.occurrences['<COLUMN-NAME>'],
    ...                          occurrenceID = occ_dwca.occurrences['<COLUMN-NAME>'])

Report After Adding Occurrence-Specific Data
---------------------------------------------------------

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 4

Next: `Scientific Names <use_scientific_name.html>`_