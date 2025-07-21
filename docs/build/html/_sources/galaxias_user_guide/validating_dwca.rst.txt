:orphan:

Validating the DwCA against GBIF 
================================

.. note::

    This is an optional step; however, validating the format of your 
    archive is recommended, as it could save you from having to fix 
    potential mistakes in your archive.

After you have successfully built your archive, now is the time to 
validate your archive against GBIF's standard.  To do this, ``galaxias`` 
has a function called ``check_archive()``, which will send your archive 
to GBIF's validator tool, and give you back a report.

.. prompt:: Python

    >>> my_dwca.check_archive()

.. program-output:: python galaxias_user_guide/check_archive_occurrences.py

Something more here.