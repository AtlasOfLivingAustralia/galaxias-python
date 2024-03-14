:orphan:

Renaming column names to Darwin Core terms
------------------------------------------------------

.. *Note:* this artice assumes you have generated an initial report.  If you have not, 
.. go `here <generate_initial_report.html>`_ and follow the instructions.

.. When we look at our generated report, we notice that a lot of things are missing:

.. .. program-output:: python galaxias_user_guide/preparing_data_script.py initial

This first step assumes that you have successfully read your data into a ``dwca`` object.  
Looking at the column names, they are not Darwin Core Terms.  To look at a list of Darwin Core 
Terms, especially for required terms by the ALA, click `here <../../getting_started/terms.html>`_.

.. prompt:: python

    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/preparing_data_script.py rename1

To rename columns so they match Darwin Core terms, we can use ``pandas``.  The following 
mapping is based on matching the current column titles in the dataset with the names of 
valid Darwin Core terms.

.. prompt:: python

    >>> temp_occurrences = my_dwca.occurrences.rename(
    ...     columns = {
    ...         "Species": "scientificName",
    ...         "Latitude": "decimalLatitude",
    ...         "Longitude": "decimalLongitude",
    ...         "Collection_date": "eventDate",
    ...     }
    ... )
    >>> temp_occurrences.head()

.. program-output:: python galaxias_user_guide/preparing_data_script.py rename2

Now, since the new column names are in a temporary variable, you need replace the old data 
frame with the new one.

.. prompt:: python

    >>> my_dwca.occurrences = temp_occurrences
    >>> my_dwca.occurrences

.. program-output:: python galaxias_user_guide/preparing_data_script.py rename3

Next, go to `Adding Uncertainty <uncertainty.html>`_