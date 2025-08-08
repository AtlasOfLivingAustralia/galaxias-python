:orphan:

Validating the DwCA against GBIF 
================================

.. note::

    This currently doesn't work very well. This will point to an ALA validator 
    in the future, and should be used with caution.

After you have successfully built your archive, you might want to 
validate your archive against the GBIF API.  To do this, ``galaxias`` 
has a function called ``check_archive()``, which will send your archive 
to GBIF's validator tool, and give you back a report.

.. prompt:: Python

    >>> my_dwca.check_archive()

.. program-output:: python galaxias_user_guide/check_archive_occurrences.py