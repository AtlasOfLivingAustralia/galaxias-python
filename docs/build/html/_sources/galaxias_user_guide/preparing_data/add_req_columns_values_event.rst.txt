:orphan:

Adding required columns and values
-----------------------------------

Now, we will check for further required columns and values.

.. prompt:: python

    >>> my_dwca.generate_data_report()

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 9

Sometimes you will need to add certain information to be able to submit data to an atlas.  For the ALA, we require 
not only taxon information (``scientificName``, etc), latitude and longitude (``decimalLatitude`` and ``decimalLongitude``) 
as well as the date on which the species was spotted (``eventDate``), we will also require other fields:

- ``eventID``
- ``parentEventID``
- ``eventType``
- ``eventDate``
- ``Event``
- ``samplingProtocol``

For ``Event`` and ``samplingProtocol``, you can set one value for all your occurrences using ``pandas``.  
If you need to set them individually, then manually adding a column is likely best.

.. warning::

    All of these columns should be looked over manually, as you can include different sampling protocols for each 
    event, ``eventDate`` will change, and ``eventID`` and ``parentEventID`` are going to be linked.

To add these columns and default values to them:

.. prompt:: python

    >>> my_dwca.occurrences["samplingProtocol"] = "observation"

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 10


For ways to prepare your occurrence data, go back to `the "Preparing Data" main page <../preparing_occurrence_data.html>`_.