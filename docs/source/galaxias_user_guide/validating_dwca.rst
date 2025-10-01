:orphan:

Validating the DwCA against GBIF 
================================

There are two ways to check whether the contents of your Darwin Core Archive meet the Darwin Core Standard.

The first is to run local tests on the files inside a local folder directory that will be used to build a 
Darwin Core Archive. ``check_directory()`` allows us to check ``csv`` files and ``xml`` files in the directory 
against Darwin Core Standard criteria, using the same checking functionality that is built into the ``set_`` 
functions. This function is especially beneficial if you have standardized your data to Darwin Core headers 
using functions outside of ``galaxias`` / ``corella``.

.. prompt:: Python

    >>> galaxias.check_directory()

The second is to check whether a complete Darwin Core Archive meets institution’s Darwin Core criteria via an API. 
For example, we can test an archive against GBIF’s API tests.

.. prompt:: Python

    >>> my_dwca.check_archive(archive="dwc-dwca.zip",
    ...                       email="your-email",
    ...                       username = "your-username",
    ...                       password = "your-password")