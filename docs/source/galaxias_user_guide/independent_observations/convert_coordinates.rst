.. _convert_coordinates:

What if your coordinates are in degrees minutes seconds?
==================================================================

The Atlas of Living Australia, and many other atlases, will report occurrence records as 
degrees latitude and degrees longitude in the Coordinate Reference System WGS84.  However, 
we acknowledge there are many formats to measure latitude and longitude.  Here, we will take 
you through how to convert your coordinates from these other common systems of measurement 
into degrees latitude and longitude.

Thankfully, there is a great package for this called `lat_lon_parser <https://github.com/NOAA-ORR-ERD/lat_lon_parser>`_.  
To install this package, type the following command into a terminal:

.. prompt:: bash

    pip install lat-lon-parser

Here, we will show you a few examples of converting different formats to degrees latitude and 
degrees longitude.

Converting Degrees Minutes Seconds
-----------------------------------

Let's say you have the latitude coordinate ``35° 50' 11"`` and the longitude coordinate 
``138° 01' 26"``.  To convert them using the ``lat-lon-parser``, type

.. prompt:: python

    >>> from lat_lon_parser import parse 
    >>> parse("35\° 50' 11\"")
    >>> parse("138\° 01\' 26\"")

.. program-output:: python -c "from lat_lon_parser import parse;print(parse('35\° 50\' 11\"'));print(parse('138\° 01\' 26\"'))"

The package will expect the text in order of degrees minutes seconds, with the appropriate signs and 
the numbers having a separator.  The back slashes tell Python that those are special characters, rather 
than the beginnings and ends of strings or other things

If you want to loop over your data frame containing these types of numbers, you can run something 
like the following example:

.. prompt:: python

    >>> from lat_lon_parser import parse
    >>> import pandas as pd 
    >>> occ = pd.DataFrame(
    ...     {
    ...         'decimalLatitude': ["35\° 50' 11\"", "45\° 51' 13\"", "30\° 20' 10\""], 
    ...         'decimalLongitude': ["138\° 01\' 26\"", "139\° 11\' 16\"", "128\° 05\' 29\""]
    ...     }
    ... )
    >>> for i, row in occ.iterrows():
    ...     occ.at[i, 'decimalLatitude'] = round(parse(row['decimalLatitude']),2)
    ...     occ.at[i, 'decimalLongitude'] = round(parse(row['decimalLongitude']),2)
    >>> occ

.. program-output:: python galaxias_user_guide/independent_observations/convert_coords.py

Here, we have converted a ``pandas DataFrame`` containing coordinates in degrees minutes seconds 
to decimal degrees, and have rounded the answer to two decimal places.  This is to ensure 
good rounding practices, as well as fewer digits in the converted number.