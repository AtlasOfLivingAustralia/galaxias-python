.. _set_datetime:

set_datetime
======================================

One of the functions you can use to check certain columns of your data is ``set_datetime()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``eventDate``: the date of your observation

It can also (optionally) can check the following:

- ``eventTime``: year of your observation
- ``year``: year of your observation
- ``month``: year of your observation
- ``day``: year of your observation

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> events = pd.read_csv('<YOUR-FILENAME>.csv')

``eventDate`` with Events
====================================================

As ``eventDate`` occurs in both your ``occurrences`` data, as well as the ``events`` data, you can 
use the function ``set_datetime()`` for both.  For events, however, you have to set the argument 
``check_events`` to ``True``.  In addition, seince we konw that we have dates, we can specify the 
``eventDate``  column to be ``'date'``.

.. prompt:: python

    >>> my_dwca.set_datetime(check_events=True,
    ...                      eventDate='date')

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 9

We get an error here because ``set_datetime()`` requires the ``eventDate`` column to be in a ``datetime`` 
format.  This is to make sure the date is formatted correctly.  Luckily, ``set_datetime()`` has a few 
arguments that will convert dates in strings to ``datetime`` format.  

- ``string_to_datetime``: when this is set to ``True``, will convert any strings in the ``eventDate`` column to ``datetime`` objects.
- ``yearfirst``: when this is set to ``True``, ``corella`` (and ``pandas``) assumes your date starts with the year.
- ``dayfirst``: when this is set to ``True``, ``corella`` (and ``pandas``) assumes your date starts with the day.

Note when both ``yearfirst`` and ``dayfirst`` are set to ``False``, ``pandas`` assumes month is first.

.. prompt:: python

    >>> my_dwca.set_datetime(dataframe=events,
    ...                      eventDate='date',
    ...                      string_to_datetime=True,
    ...                      yearfirst=False,
    ...                      dayfirst=True)

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 10

what does ``check_data`` and ``suggest_workflow`` say now? 
=============================================================

*Note:* each of the ``set_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> my_dwca.check_data(events=events)

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 11

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> my_dwca.suggest_workflow(dataframe=events)

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 12

Other functions
=====================================

To learn more about how to use these functions, go to 

- `set_events <set_events.html>`_

Optional functions:

- `set_abundance <set_abundance_events>`_
- `set_locality <set_locality_events.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_