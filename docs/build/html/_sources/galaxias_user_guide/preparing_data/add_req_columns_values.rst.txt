:orphan:

Adding required columns and values
-----------------------------------

Now, we will check for further required columns and values.

.. prompt:: python

    >>> my_dwca.generate_data_report()

.. program-output:: python galaxias_user_guide/preparing_data_script.py add_reqs1

Sometimes you will need to add certain information to be able to submit data to an atlas.  For the ALA, we require 
not only taxon information (``scientificName``, etc), latitude and longitude (``decimalLatitude`` and ``decimalLongitude``) 
as well as the date on which the species was spotted (``eventDate``), we will also require other fields:

- ``coordinateUncertaintyInMeters``: this is the uncertainty associated with any occurrence record.  This can be something like the error associated with your GPS or phone.  A good default, if you're unsure, is ``100``.
- ``geodeticDatum``: this refers to the Coordinate Reference System (CRS) of how you recorded your data.  For example, if you used your GPS, your CRS would likely be something called ``WSG84``, which is the standard CRS for many GPSs.
- ``basisOfRecord``: this is how the record was taken.  For example, if you observed all of these occurrences, then you would set the value of ``basisOfRecord`` to ``HumanObservation``.
- ``occurrenceID`` / ``catalogNumber``/ ``recordNumber``: a unique value associated with this specific occurrence.

For ``coordinateUncertaintyInMeters``, ``geodeticDatum`` and ``basisOfRecord``, you can set one value for all your 
occurrences using ``pandas``.  If you need to set them individually, then manually adding a column is likely best.

To add these columns and default values to them:

.. prompt:: python

    >>> my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    >>> my_dwca.occurrences["geodeticDatum"] = "WGS84"
    >>> my_dwca.occurrences["basisOfRecord"] = "HumanObservation"
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/preparing_data_script.py add_reqs2

For adding an ``occurrenceID`` / ``catalogNumber``/ ``recordNumber``, this is a bit different.  Each occurrence has 
to have a different unique ID.  We have written a function that will do this automatically, with you only having 
to specify the column name you wish to use.

.. prompt:: python

    >>> my_dwca.add_unique_occurrence_IDs(column_name="occurrenceID")
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/preparing_data_script.py add_reqs3

For more ways to prepare your data, go back to `the "Preparing Data" main page <../preparing_data.html>`_.