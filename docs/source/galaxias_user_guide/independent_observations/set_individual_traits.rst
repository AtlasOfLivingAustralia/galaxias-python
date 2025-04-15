.. _set_individual_traits:

set_individual_traits
---------------------------

.. Note:: 
    
    Individual trait data is not required by the ALA, but it is nice to have.

One of the functions you can use to check your data is ``set_individual_traits()``.  
This function aims to check if you have the following:

- ``individualID``: An identifier for an individual or named group of individual organisms represented in the Occurrence. Meant to accommodate resampling of the same individual or group for monitoring purposes. May be a global unique identifier or an identifier specific to a data set.
- ``lifeStage``: The age class or life stage of an organism at the time of occurrence.
- ``sex``: The sex of the biological individual.
- ``vitality``: An indication of whether an organism was alive or dead at the time of collection or observation.
- ``reproductiveCondition``: The reproductive condition of the biological individual.

specifying individual organism information
--------------------------------------------

If you are looking at individual organisms, recording additional trait information is possible in 
the Darwin Core standard.  An example is below:

.. prompt:: python

    >>> import pandas as pd
    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    >>> my_dwca = my_dwca.dwca(occurrences=occ)
    >>> my_dwca.set_individual_traits(dataframe=occ,individualID=['123456','123457'],
    ...                               lifeStage='adult',sex=['male','female'],
    ...                               vitality='alive',reproductiveCondition='not reproductive')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 33

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
- `set_license <set_license.html>`_
- `set_locality <set_locality.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_