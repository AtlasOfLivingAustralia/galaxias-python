:orphan:

Adding Dates and Times
============================

The ALA also requires you to have the date on which you observe the species.  This is specified 
by the ``eventDate`` column.  These need to be in ``datetime`` data type, using the `datetime 
<https://docs.python.org/3/library/datetime.html>`_ package from Python.

First, let's see what is in our occurrences dataframe:

.. prompt:: Python

    >>> occ_dwca.occurrences.head()

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 10

If we try ``use_datetime()`` on the data, we will get an error because our dates are a string:

.. prompt:: Python

    >>> occ_dwca.use_datetime()

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 11

Thankfully, ``use_datetime()`` has an argument called ``string_to_datetime``, which will let ``galaxias`` 
know to convert all your dates in the ``eventDate`` column into the ``datetime`` type.  Before you do this, 
however, you will need to specify what format your ``eventDate`` column is in.  To do this, you will need to 
specify the order of the day, month, and year (as well as hours, minutes and seconds if applicable).  You 
will need to specify the order as a string.  Here are how you specify each component:

- year: ``%Y``
- month: ``%m``
- day: ``%d``
- hours: ``%H``
- minutes: ``%M``
- seconds: ``%S``

Then, to separate these components, you will also need to add what separates our components.  In our 
example, the ``/`` character separates them, so our ``orig_format`` will be ``'%d/%m/%Y'``.

.. prompt:: Python 

    >>> my_dwca.use_datetime(eventDate=my_dwca.occurrences['Collection_date'],
    ...                      string_to_datetime=True,
    ...                      orig_format='%d/%m/%Y')

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 12

Now all the dates and times are in the correct format.  By default, the time added will be ``00:00:00`` and 
the time zone will be assumed to be UTC (Coordinated Universal Time).

Report After Adding Date and Time Data
---------------------------------------------------------

Now, we will see what the data is like after changing the dates:

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 13

OPTIONAL: `Adding Additional Location Data <additional_geo.html>`_

Start Preparing Metadata: `Preparing Metadata <../preparing_metadata.html>`_