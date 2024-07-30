:orphan:

Using Scientific Names
===========================

With scientific names, the Atlas of Living Australia requires the scientific name of each species you observed.  The Atlas uses 
The National Species List in Australia, and also draws on the New Zealand Organism Register and Catalogue of Life.  At this stage, 
we will not check whether or not your name matches with the Atlas' backbone; instead, we will check whether or not the column is 
present and whether your data is in the correct format.  To do this, run the following:

.. prompt:: Python

    >>> occ_dwca.use_scientific_name(scientific_name = occ_dwca.occurrences['Species'])

Your data will look like this:

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 5

Report After Adding Scientific Name Data
---------------------------------------------------------

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 6

Next: `Location Data <use_coordinates.html>`_