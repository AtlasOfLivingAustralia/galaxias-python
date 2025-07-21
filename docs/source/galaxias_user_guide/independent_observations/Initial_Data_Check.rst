.. _Initial Data Check:

Initial Data Check
--------------------

When you're ready to start submitting your data, there are a number of things to 
check to ensure the ingestion process into the ALA is smooth.  Some of this is ensuring 
that your column names conform to Darwin Core Vocabulary standards, and that your 
data is in the correct format (i.e. numerical columns are actually numerical).  

For these examples, we will be using the the dataset linked above.  If, however, you want to 
go through this workflow using your own data, please feel free to do so!  

To read in the data you want to use, you're going to use ``pandas`` to read in the csv file as a table.

.. prompt:: python

    >>> import galaxias
    >>> import pandas as pd
    >>> my_archive = galaxias.dwca(occurrences='<YOUR-FILENAME>.csv')

Now that you have a dataframe with data in it, we can check the data using the 
function ``galaxias.check_dataset()``. 

.. prompt:: python

    >>> galaxias.check_dataset()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 1

For our initial data example, the data tests may not be showing any errors, but 
unfortunately, this means no column names were checked.  This is because the names 
of the columns are not part of the standard Darwin Core Vocabulary.  Thankfully, 
we have created a series of functions that can help you get your data into the 
Darwin Core standard.  To show the functions ``galaxias`` contains that can help you 
do this, we have developed an all-purpose function called ``suggest_workflow()``.  Here 
are the results of this particular dataset:                                  

.. prompt:: python

    >>> galaxias.suggest_workflow()

.. program-output:: python galaxias_user_guide/independent_observations/data_cleaning.py 2

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
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_