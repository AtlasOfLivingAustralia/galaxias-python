:orphan:

Renaming occurrence names to EventCore terms
------------------------------------------------------

*Note:* this artice assumes you have generated an initial report.  If you have not, 
go `here <generate_initial_report.html>`_ and follow the instructions.

When we look at our generated report, we notice that a lot of things are missing:

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 1

There are a lot of columns missing. However, if we look at the data we have using 
the ``head`` command of the occurrences dataframe, we can see that none of the column 
names are terms found in the Darwin Core Standard (for a list of required and 
recommended terms for your living atlas, see `a table of dwc terms <../../getting_started/terms.html>`_).

.. prompt:: python

    >>> my_dwca.occurrences.head()

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 2

Renaming columns using occurrences as an example
---------------------------------------------------

To rename columns so they match Darwin Core terms, we can use ``pandas``.  The following 
mapping is based on matching the current column titles in the dataset with the names of 
valid Darwin Core terms that are required by the ALA.

.. prompt:: python

    >>> temp_occurrences = my_dwca.occurrences.rename(
    ...     columns = {
    ...         "Species": "scientificName",
    ...         "Latitude": "decimalLatitude",
    ...         "Longitude": "decimalLongitude",
    ...         "Collection_date": "eventDate",
    ...         "number_birds": "individualCount"
    ...     }
    ... )
    >>> temp_occurrences.head()

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 3

Now, since the new column names are in a temporary variable, you need replace the old data 
frame with the new one.

.. prompt:: python

    >>> my_dwca.occurrences = temp_occurrences
    >>> my_dwca.occurrences

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 4

This same workflow can also be done for the ``events`` dataframe.

..
    Extensions
    ---------------

    We can do this with all of the data frames that we have: ``events``, ``occurrences``, ``multimedia`` and ``emof`` (extended Measurement or Fact).

    ``events``

    .. prompt:: python

        >>> my_dwca.events.head()
        >>> temp_events = my_dwca.events.rename(
        ...     columns = {
        ...         ": "Event"
        ...     }
        ... )
        >>> my_dwca.events = temp_events

    .. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 5

    ``multimedia``

    .. prompt:: python

        >>> my_dwca.multimedia.head()
        >>> temp_multimedia = my_dwca.multimedia.rename(
        ...     columns = {
        ...         "photo": "identifier"
        ...     }
        ... )
        >>> my_dwca.multimedia = temp_multimedia

    .. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 6

    ``emof``

    .. prompt:: python

        >>> my_dwca.emof.head()
        >>> temp_emof = my_dwca.emof.rename(
        ...     columns = {
        ...         "measurement": "measurementType",
        ...         "value": "measurementValue",
        ...         "unit": "measurementUnit",
        ...     }
        ... )
        >>> my_dwca.emof = temp_emof

    .. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 7

Final data report after Renaming
----------------------------------

Now that we know all of our column headings are Darwin Core compliant, we can check what 
errors we will get now.

.. prompt:: python

    >>> my_dwca.generate_data_report()

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 8

There are still a few errors, but luckily you can do these in any order in the next section, 
`Validating Data Against EventCore Standards <../preparing_eventcore.html>`_