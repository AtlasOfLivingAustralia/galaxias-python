:orphan:

Publishing Your DwCA to the ALA 
================================

.. note::

    This is our current way of submitting data, but we are working on a publication 
    API and submission portal.  Stay tuned!

Considerations before submission
---------------------------------------

After successfully building and validating your archive, now you can
publish your data to the ALA!  Before using the ``submit_archive()`` 
function to open a Github issue and submit your data, here are a few 
questions to ask yourself:

- Do I have precise coordinates of sensitive species?
- Do I want to have my data publicly available on Github before being ingested into the ALA?

If your answers to any/all of these questions is 'No', please send us your file 
and a brief description to  
`our support queue <mailto:support@ala.org.au>`_.

Submitting your data 
---------------------------------------

If you are ok with your data being in 
the public space, you can create a Github issue by using the ``submit_archive()`` 
function:

.. prompt:: Python

    >>> my_dwca.submit_archive()

This will (currently) open a browser to a Github repository titled ``data-publication``.
Drag and drop your archive here, and provide a brief description of your dataset.