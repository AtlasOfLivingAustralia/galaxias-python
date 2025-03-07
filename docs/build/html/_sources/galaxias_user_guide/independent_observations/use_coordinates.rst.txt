.. _use_coordinates:

use_coordinates
--------------------

One of the functions you can use to check certain columns of your data is ``use_coordinates()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``decimalLatitude``: the latitude of your observation
- ``decimalLongitude``: the latitude of your observation
- ``geodeticDatum``: the coordinate reference system (CRS) of your latitude and longitude

It can also (optionally) can check the following:

- ``coordinateUncertaintyInMeters``: uncertainty of your measurements in meters
- ``coordinatePrecision``: uncertainty of your measurements in decimal degrees

Specifying ``decimalLatitude`` and ``decimalLongitude``
============================================================

Since we have latitude and longitude columns, we can specify them in the 
``use_coordinates()`` function, and the columns will be renamed and the 
values checked to see if i) they are numeric; and ii) if they are in the 
correct ranges.

.. prompt:: python

    >>> my_dwca.use_coordinates(decimalLatitude='Latitude',
    ...                         decimalLongitude='Longitude')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 15

.. note:: Non-numeric values

    If you get an error saying some latitude and longitude values are not numeric, 
    that's ok!  Luckily, ``pandas`` has a function called ``to_numeric`` which will
    convert strings to numeric values for you (assuming those strings are numbers).  
    Below is an example of how to convert a column to all numeric values.  Once this 
    is completed, you can use the command above.

    .. prompt:: python

        >>> my_dwca.occurrences['latitude'] = pd.to_numeric(my_dwca.occurrences['latitude'],errors='coerce')

``geodeticDatum``
=====================================

Another required field is called ``geodeticDatum``.  This column is required as 
it lets others know how you measured latitude and longitude.  ``geodeticDatum`` 
refers to a Coordinate Reference System (CRS), which is how three-dimensional 
coordinates are represented on a two-dimensional surface.  The most common CRS 
(and what GPSs, as well as the ALA, uses) is called WGS84.  If you know that this 
is the CRS you have used, you can set the default value of ``geodeticDatum`` in 
``use_coordinates()``.

.. prompt:: python

    >>> my_dwca.use_coordinates(decimalLatitude='Latitude',
    ...                         decimalLongitude='Longitude',
    ...                         geodeticDatum='WGS84')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 17

Adding Uncertainty
=====================================

There is always uncertainty in measurements of  and longitude; however, 
sometimes it is useful to include this, especially if you know the uncertainty of 
your instruments or measurements.  If you know this information and want to include 
it, you can specify a default value (similar to the ``geodeticDatum`` column above) 
to either ``coordinatePrecision`` or ``coordinateUncertaintyInMeters``.  The former is 
in decimal degrees, and the latter is in meters.

.. prompt:: python

    >>> my_dwca.use_coordinates(dataframe=occ,
    ...                         decimalLatitude='Latitude',
    ...                         decimalLongitude='Longitude',
    ...                         geodeticDatum='WGS84',
    ...                         coordinatePrecision=0.1)
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 18

what does ``check_data`` and ``suggest_workflow`` say now? 
===========================================================

*Note:* each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> my_dwca.check_data()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 19

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> my_dwca.suggest_workflow()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 20

Other functions:
=====================================

To learn more about how to use these functions, go to 

- `use_occurrences <use_occurrences.html>`_
- `use_datetime <use_datetime.html>`_
- `use_scientific_name <use_scientific_name.html>`_

Optional functions:

- `use_abundance <use_abundance.html>`_
- `use_locality <use_locality.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_