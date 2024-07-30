:orphan:

Adding Location Data
================================

For the ALA, we require latitude and longitude (``decimalLatitude`` and ``decimalLongitude``) 
as well as the date on which the species was spotted (``eventDate``), we will also require other fields:

- ``decimalLatitude``: latitude of your observation in decimal degrees.  Must be between -90 and 90.
- ``decimalLongitude``: longitude of your observation in decimal degrees.  Must be between -180 and 180.
- ``geodeticDatum``: this refers to the Coordinate Reference System (CRS) of how you recorded your data.
- ``coordinateUncertaintyInMeters``: denotes radius of uncertainty around a measurement (in meters)
- ``coordinatePrecision``: denotes the precision of your measuring instrument in degrees

Choosing Your Latitude and Longitude Columns
----------------------------------------------

For the latitude and longitude columns, ``galaxias`` assumes you will have location data for your occurrences already.  To 
make sure the columns have the correct name, type

    >>> occ_dwca.use_coordinates(decimalLatitude=occ_dwca.occurrences['Latitude'],
    ...                          decimalLongitude=occ_dwca.occurrences['Longitude'])
    >>> occ_dwca.occurrences.head()

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 7

Setting Your ``geodeticDatum`` and uncertainties
----------------------------------------------------

``geodeticDatum``, to expand upon above, is a way of measuring coordinates on a 2-dimensional surface, taking into account 
the curvature of the Earth in these calculations.  If you used your GPS or your phone, your CRS would likely be the same as 
the Atlas of Living Australia.  This is because both the Atlas and most GPSes use the World Standard called ``WSG84`` (`World 
Geodetic System 84 <https://en.wikipedia.org/wiki/World_Geodetic_System>`_).

``coordinateUncertaintyInMeters`` and ``coordinatePrecision`` are both measurements of uncertainty, but the former denotes the inherent 
uncertainty in the measurement itself, and the latter denotes the uncertainty in the device you are using to take the measurement.  
A good default to use is ``100`` for ``coordinateUncertaintyInMeters``, and ``0.01`` for ``coordinatePrecision``. 

If you don't have these measurements in your data, like the example data, you can add them in using ``use_coordinates``:

.. prompt:: Python

    >>> occ_dwca.use_coordinates(geodeticDatum='WGS84',
    ...                          coordinateUncertaintyInMeters=100,
    ...                          coordinatePrecision=0.01)
    >>> occ_dwca.occurrences.head()

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 8

Alternatively, if you have these columns in your data but they don't have the correct name, you can use the columns instead of the 
values.

.. prompt:: Python

    >>> occ_dwca.use_coordinates(geodeticDatum=occ_dwca.occurrences['<COLUMN_NAME>'],
    ...                          coordinateUncertaintyInMeters=occ_dwca.occurrences['<COLUMN_NAME>'],
    ...                          coordinatePrecision=occ_dwca.occurrences['<COLUMN_NAME>'])

Putting It All Together
--------------------------

If you don't want to do these two parts separately, you can combine them all in one:

.. prompt:: Python

    >>> occ_dwca.use_coordinates(decimalLatitude=occ_dwca.occurrences['latitude'],
    ...                          decimalLongitude=occ_dwca.occurrences['longitude'],
    ...                          geodeticDatum='WGS84',
    ...                          coordinateUncertaintyInMeters=100,
    ...                          coordinatePrecision=0.01)

Report After Adding Location Data
---------------------------------------------------------

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 9

Next: `Adding Date and Times <use_datetime.html>`_