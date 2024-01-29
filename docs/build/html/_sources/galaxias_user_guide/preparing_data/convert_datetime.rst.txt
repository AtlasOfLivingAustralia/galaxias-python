:orphan:

Converting Dates into YYYY-MM-DD or format including timestamps
==================================================================

For this exercise, we will be using the ``datetime`` package and string manipulation.  Users should 
have ``datetime`` on their initial install of ``Python``.

For the Atlas of Living Australia, they require dates to either be in the format of ``YYYY-MM-DD`` or 
in ``iso`` format, which is ``YYYY-MM-DDTHH:MM:SS``.

``DD-MM-YYYY`` and ``MM-DD-YYYY`` formats
-------------------------------------------

First, we will look at the ``DD-MM-YYYY`` format.

.. prompt:: python

    >>> # DD-MM-YYYY
    >>> date = "01-05-2005"
    >>> split_date = date.split("-")
    >>> new_date = "-".join(list(reversed(split_date)))
    >>> new_date

.. program-output:: python -c "date = '01-05-2005';split_date = date.split('-');new_date = '-'.join(list(reversed(split_date)));print(new_date)"

Converting the ``MM-DD-YYYY`` format is a bit tricker, but still can be done in the same number of 
lines of code.

.. prompt:: python

    >>> # DD-MM-YYYY
    >>> date = "05-01-2005"
    >>> split_date = date.split("-")
    >>> new_date = "-".join([split_date[2],split_date[0],split_date[1]])
    >>> new_date

.. program-output:: python -c "date = '05-01-2005';split_date = date.split('-');new_date = '-'.join([split_date[2],split_date[0],split_date[1]]);print(new_date)"

Now, if we want to put it in a loop:

.. prompt:: python

    >>> # DD-MM-YYYY
    >>> import pandas as pd
    >>> dates =  pd.DataFrame(
    ...     {
    ...         "eventDate": ["05-01-2005","22-02-2022","5-5-2005","21-9-2021"]
    ...     }
    ... )
    >>> for i,row in dates.iterrows():
    ...     split_date = row["eventDate"].split("-")
    ...     dates.at[i,"eventDate"] = "-".join(list(reversed(split_date)))
    >>> dates

.. program-output:: python galaxias_user_guide/preparing_data/convert_datetime.py


``YYYY-MM-DDTHH:MM:SS`` (``iso`` format)
------------------------------------------

For some species, having the times at which they are spotted can be helpful, especially if they 
are a nocturnal species.  The Atlas of Living Australia requires them to be in ``iso`` format.  
Luckily, the ``datetime`` package handes this.

.. prompt:: python 

    >>> import datetime
    >>> date_and_time = "01-05-2005 18:30"
    >>> date, time = date_and_time.split(" ")
    >>> split_date = list(map(int, date.split("-")))
    >>> split_time = list(map(int, time.split(":")))
    >>> datetime.datetime(split_date[2],split_date[1],split_date[0],split_time[0],split_time[1]).isoformat()

.. program-output:: python -c "import datetime;date_and_time = '01-05-2005 18:30';date, time = date_and_time.split(' ');split_date = list(map(int, date.split('-')));split_time = list(map(int, time.split(':')));print(datetime.datetime(split_date[2],split_date[1],split_date[0],split_time[0],split_time[1]).isoformat())"

For other checks of your data, go back to the `data homepage <../preparing_data.html>`_.