.. _What Does A Passing Occurrences Dataset Look Like?:

What Does A Passing Occurrences Dataset Look Like?
-------------------------------------------------------

If you've gone through all the steps outlined for the example 
occurrences dataset, your final step(s) will look like the following: 

.. prompt:: python

    >>> # this is each individual step as a command
    >>> import pandas as pd
    >>> import galaxias
    >>> my_dwca = galaxias.dwca(occurrences = '<FILENAME>.csv')
    >>> my_dwca.use_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID=True
    ...       ).use_scientific_name(scientificName='Species'
    ...       ).use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',geodeticDatum='WGS84',coordinatePrecision=0.1
    ...       ).use_datetime(eventDate='Collection_date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    >>> my_dwca.check_dataset()

And your final output from ``check_data()`` will look like this:

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 31