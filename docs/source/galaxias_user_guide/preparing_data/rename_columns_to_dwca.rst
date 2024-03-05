:orphan:

Renaming column names to Darwin Core terms
------------------------------------------------------

*Note:* this artice assumes you have generated an initial report.  If you have not, 
go `here <generate_initial_report.html>`_ and follow the instructions.

When we look at our generated report, we notice that a lot of things are missing:

.. program-output:: python galaxias_user_guide/preparing_data_script.py initial

There are a lot of columns missing. However, if we look at the data we have using 
the ``head`` command of the occurrences dataframe, we can see that none of the column 
names are terms found in the Darwin Core Standard (for a list of required and 
recommended terms for your living atlas, see `a table of dwc terms <../../getting_started/terms.html>`_).

.. prompt:: python

    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/preparing_data_script.py rename1

To rename columns so they match Darwin Core terms, we can use ``pandas``.  The following 
mapping is based on matching the current column titles in the dataset with the names of 
valid Darwin Core terms that are required by the ALA.

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

Now that we know all of our column headings are Darwin Core compliant, we can check what 
errors we will get now.

.. prompt:: python

    >>> my_dwca.occurrences = temp_occurrences
    >>> my_dwca.occurrences

.. program-output:: python galaxias_user_guide/preparing_data_script.py rename4    

There are still a few errors, but luckily you can do these in any order in the next section, 
`Validating Data Against DwC Standards <../preparing_data.html>`_