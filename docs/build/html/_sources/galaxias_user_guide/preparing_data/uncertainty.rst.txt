:orphan:

Uncertainty
==============

Every measurement of latitude and longitude has some degree of uncertainty associated with it.  It is 
important to capture this, either in degrees latitude/longitude or in meters.  To this end, there are 
two Darwin Core terms that you can use for this:

- ``coordinatePrecision``
- ``coordinateUncertaintyInMeters``

According to the webpages on `coordinate precision <https://dwc.tdwg.org/list/#dwc_coordinatePrecision>`_ and 
`coordinate uncertainty in meters <https://dwc.tdwg.org/list/#dwc_coordinateUncertaintyInMeters>`_, they 
can vary widely (for example, coordinate precision can vary from 0.00001, which is the normal GPS limit for 
decimal degrees, to 1.0, which is to the nearest degree).  If this is unknown, leave it blank.

If you do know the precision or uncertainty, and it is the same for all the data, you can add a column to 
your dataframe by using the command below, as an example:

.. prompt:: python

    >>> my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100

To see an example of a passing report, go to `preparing data <../preparing_data.html>`_.