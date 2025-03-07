.. _adding_eventID_occurrences:

how to add eventIDs to your occurrences file
---------------------------------------------

Thus far, we have only talked about setting up events and occurrence files individually.  
However, they need to be linked by a common key so we know which occurrences were seen 
at which event.  Thus, we will link them via the ``eventID`` column.

This step assumes that you have set up both your occurrence and event dataframes using the 
previous tutorials.  If you haven't, in the dropdown menu is the code for your perusal.

.. dropdown:: Code for occurrences and events thus far

    .. prompt:: python

        >>> events = my_dwca.use_events(dataframe=events,
        ...                             eventType='type',
        ...                             samplingProtocol='Observation',
        ...                             Event='name',
        ...                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
        >>> events = my_dwca.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
        >>> occ = my_dwca.use_occurrences(dataframe=occ,
        ...                               basisOfRecord='HumanObservation',
        ...                               occurrenceStatus='PRESENT',
        ...                               occurrenceID=True)
        >>> occ = my_dwca.use_scientific_name(dataframe=occ,
        ...                                   scientificName='Species')
        >>> occ = my_dwca.use_coordinates(dataframe=occ,
        ...                               decimalLatitude='Latitude',
        ...                               decimalLongitude='Longitude',
        ...                               geodeticDatum='WGS84',
        ...                               coordinatePrecision=0.1)
        >>> occ = my_dwca.use_datetime(dataframe=occ,
        ...                            eventDate='Collection_date',
        ...                            string_to_datetime=True,
        ...                            yearfirst=False,
        ...                            dayfirst=True)

``corella`` can automatically link your ``eventID``s in your events file to the occurrences by 
comparing whether or not the date in the ``eventDate`` column is the same.  What this looks like 
in principle is supplying three arguments:

- ``add_eventID``: set this to ``True`` if you want ``corella`` to automatically add ``eventID``s
- ``events``: provide the events dataframe containing the ``eventID``s to link.
- ``eventType``: specify the ``eventType`` that you want to link to the occurrences.  In this case, ``'Observation'`` is the appropriate term.

The command will then look like this (using one of the commands in the dropdown as a template)

.. prompt:: python

    >>> my_dwca.use_occurrences(add_eventID=True,
    ...                         occurrenceStatus='PRESENT',
    ...                         occurrenceID=True,
    ...                         add_eventID=True,
    ...                         events=events,
    ...                         eventType='Observation')

#.. program-output:: python corella_user_guide/events/events_workflow.py 13