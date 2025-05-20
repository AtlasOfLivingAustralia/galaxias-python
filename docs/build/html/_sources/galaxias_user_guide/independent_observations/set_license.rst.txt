.. _set_license:

set_license
---------------------------

.. Note:: 
    
    License information in the data itself is not required by the ALA, but it is nice to have.

One of the functions you can use to check your data is ``set_individual_traits()``.  
This function aims to check if you have the following:

- ``license``: A legal document giving official permission to do something with the resource. Must be provided as a url to a valid license.
- ``rightsHolder``: Person or organisation owning or managing rights to resource.
- ``accessRights``: Access or restrictions based on privacy or security.

specifying license information
--------------------------------------------

For specifying license information for individual organisms, as well as the rights holders, use the example below:

.. prompt:: python

    >>> import pandas as pd
    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    >>> my_dwca = galaxias.dwca(occurrences=occ)
    >>> my_dwca.set_license(dataframe=occ,license=['CC-BY 4.0 (Int)', 'CC-BY-NC 4.0 (Int)'],
    ...                           rightsHolder='The Regents of the University of California',
    ...                           accessRights=['','not-for-profit use only'])
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 34

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_
- `set_collection <set_collection.html>`_
- `set_individual_traits <set_individual_traits.html>`_
- `set_locality <set_locality.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_