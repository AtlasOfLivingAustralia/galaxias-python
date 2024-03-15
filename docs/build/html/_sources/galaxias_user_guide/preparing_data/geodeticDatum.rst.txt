:orphan:

``geodeticDatum``
====================

``geodeticDatum`` is specifying how your latitude and longitude measurements are represented.  Simply put, there 
are many ways to measure coordinates on the curvature of the earth, in what's called a "Coordinate Reference System".  
The Atlas of Living Australia uses the `WGS84 <https://en.wikipedia.org/wiki/World_Geodetic_System>`_ standard, which 
is what your GPS uses.

If you used a single GPS to record your latitude and longitude measurements, you can add a column denoting the 
Coordinate Reference System into your occurrences by doing the following:

.. prompt:: python

    >>> my_dwca.occurrences["geodeticDatum"] = "WGS84"

Next: `basisOfRecord <basisOfRecord.html>`_