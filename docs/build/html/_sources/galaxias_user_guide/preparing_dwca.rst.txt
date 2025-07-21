:orphan:

Preparing the DwCA itself 
==========================

Preparing your Darwin Core Archive is a straightforward process.  
However, this also assumes that you have already prepared your data 
and metadata to comply with Darwin Core standards.  If you have not done 
this, please see our vignettes on preparing an 
`independent observations dataset <independent_observations/index.html>`_ 
or a `longitudinal studies dataset <longitudinal_studies/index.html>`_.

Creating a Darwin Core Archive
-------------------------------------------

When your data passes all of the internal data checks, and you have 
written out your metadata statement into XML format, you can then 
run the ``create_dwca()`` function.

.. prompt:: Python

    >>> my_dwca.build_archive()

Before this function creates the archive file, it will again check your 
data and metadata.  If something doesn't comply with Darwin Core standards, 
you will get an error message.  If everything passes, this will produce a 
Darwin Core Archive titled ``dwca.zip``, which contains all of your data 
and metadata, and is located in the ``data-publish`` folder in your 
current working directory.  