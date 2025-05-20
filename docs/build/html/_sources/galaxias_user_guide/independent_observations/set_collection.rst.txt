.. _set_collection:

set_collection
--------------------

.. Note:: 
    
    Collection information is not required by the ALA, but it is nice to have.

One of the functions you can use to check your data is ``set_collection()``.  
This function aims to check if you have the following:

- ``datasetID``: An identifier for the set of data. May be a global unique identifier or an identifier specific to a collection or institution.
- ``datasetName``: The name identifying the data set from which the record was derived.
- ``catalogNumber``: A unique identifier for the record within the data set or collection.

Specifying Collection Information
--------------------------------------------

If your observation is part of a collection, adding additional information on the specimen so others 
can properly reference it is straightforward.  All the arguments above take either a ``str``  (denoting a column name 
or a higher taxon) or a ``list``.  An example of this is below:

.. prompt:: python

    >>> import pandas as pd
    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    >>> my_dwca = galaxias.dwca(occurrences=occ)
    >>> my_dwca.set_collection(dataframe=occ,datasetID='b15d4952-7d20-46f1-8a3e-556a512b04c5',
    ...                        datasetName='Lacey Ctenomys Recaptures',catalogNumber='2008.1334')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 32

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_
- `set_individual_traits <set_individual_traits.html>`_
- `set_license <set_license.html>`_
- `set_locality <set_locality.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_