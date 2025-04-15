.. _set_taxonomy:

set_taxonomy
--------------------

.. Note:: 
    
    Higher order taxonomy information is not required by the ALA, but it is nice to have.

One of the functions you can use to check your data is ``set_taxonomy()``.  
This function aims to check if you have the following:

- ``kingdom``: the kingdom of identified taxon
- ``phylum``: the phylum of identified taxon
- ``taxon_class``: the class of identified taxon.  It is specified as ``taxon_class`` here because ``class`` is denoting a ``class`` object in Python.
- ``order``: the order of identified taxon
- ``family``: the family of identified taxon
- ``genus``: the genus of identified taxon
- ``specificEpithet``: The name of the first species or species epithet of the ``scientificName``
- ``vernacularName``: The common or vernacular name of the identified taxon

specifying higher taxonomy
--------------------------------------------

.. Note:: 

    Adding this taxonomic information automatically is potentially planned for future releases of ``galaxias``.

To determine the what all the higher taxonomic information is for the ALA, visit `ala.org.au <ala.org.au>`_ and 
search for your taxon.  Each argument for ``set_taxonomy`` will either take a ``str`` (denoting a column name 
or a higher taxon) or a ``list``.  An example of this is below:

.. prompt:: python

    >>> import pandas as pd
    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    >>> my_dwca = galaxias.dwca(ooccurrences=occ)
    >>> my_dwca.set_taxonomy(dataframe=occ,kingdom='Animalia',phylum='Chordata',taxon_class='Aves',
    ...                      order='Psittaciformes',family='Cacatuidae',genus='Eolophus',
    ...                      specificEpithet='roseicapilla',vernacularName='Galah')
    >> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 31


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
- `set_license <set_license.html>`_
- `set_locality <set_locality.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_