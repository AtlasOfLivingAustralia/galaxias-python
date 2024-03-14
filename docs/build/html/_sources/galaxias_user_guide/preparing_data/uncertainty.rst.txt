:orphan:

Uncertainty
==============

- ``coordinateUncertaintyInMeters``: this is the uncertainty associated with any occurrence record. 
This can be something like the error associated with your GPS or phone.  A good default, 
if you're unsure, is ``100``. **but why tho?**

.. prompt:: python

    >>> my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100

Next, go to `Adding geodeticDatum <geodeticDatum.html>`_