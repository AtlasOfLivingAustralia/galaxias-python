.. _use_locality_events:

use_locality
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``use_locality()``.  
This function aims to check if you have the following:

- ``continent``: the latitude of your observation
- ``country``: the latitude of your observation
- ``countryCode``: the coordinate reference system (CRS) of your latitude and longitude
- ``stateProvince``: uncertainty of your measurements in meters
- ``locality``: uncertainty of your measurements in decimal degrees

specifying ``locality``
--------------------------------------------

For our example dataset, we have a column titled 'location'.  However, this is not a Darwin Core 
term, and we need to be more specific.  'Cannonvale' is a suburb, and anything that's a suburb 
will go under the ``locality`` field.

.. prompt:: python

    >>> my_dwca.use_locality(check_events = True, locality='location')

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 15

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `use_events <use_events.html>`_
- `use_datetime <use_datetime.html>`_

Optional functions:

- `use_abundance <use_abundance_events.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_