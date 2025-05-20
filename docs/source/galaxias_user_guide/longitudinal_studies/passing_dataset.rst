.. _What Does A Passing Events Dataset Look Like?:

What Does A Passing Events Dataset Look Like?
-------------------------------------------------------

*Note: This next step assumes you have done all the steps in the below code*

.. dropdown:: Code for occurrences and events for example dataset

    .. prompt:: python

        >>> # this is each individual step as a command
        >>> import pandas as pd
        >>> import galaxias
        >>>
        >>> # first, events
        >>> my_dwca=galaxias.dwca(occurrences="galaxias_user_guide/data/occurrences_event_nomulti.csv",
        ...                       events="galaxias_user_guide/data/events_use.csv")
        >>> my_dwca.set_events(eventType='type',
        ...                    samplingProtocol='Observation',
        ...                    Event='name',
        ...                    event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
        >>> my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
        >>> my_dwca.occurrences['Longitude'] = pd.to_numeric(my_dwca.occurrences['Longitude'],errors='coerce')
        >>> my_dwca.set_datetime(check_events=True,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
        >>> my_dwca.set_occurrences(basisOfRecord='HumanObservation',
        ...                         occurrenceID=True)
        >>> my_dwca.set_scientific_name(scientificName='Species')
        >>> my_dwca.set_coordinates(decimalLatitude='Latitude',
        ...                         decimalLongitude='Longitude',
        ...                         geodeticDatum='WGS84',
        ...                         coordinatePrecision=0.1)
        >>> my_dwca.set_datetime(eventDate='Collection_date',
        ...                     string_to_datetime=True,
        ...                     yearfirst=False,
        ...                     dayfirst=True)
        >>> my_dwca.set_occurrences(add_eventID=True,eventType='Observation')
        >>> my_dwca.set_abundance(individualCount='number_birds')
        >>> my_dwca.set_locality(check_events = True, locality='location')
        >>> my_dwca.check_dataset()

Before you write your metadata using ``delma`` or package your Darwin Core Archive using ``galaxias``, 
run ``check_data()`` for the final time.

.. prompt:: python

    >> galaxias.check_data()

If everything passes, you will get the following output:

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 16