:orphan:

Checking taxonomy
--------------------------------

Now that we have renamed the data columns, let's check how our taxonomy compares with the ALA backbone.  To start,
let's generate another data report to see how renaming our columns changes the report.

.. prompt:: python

    >>> my_dwca.generate_data_report()

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 9

Here, we can see that there are a few species names that are either misspelled or differ slightly from what is 
available at the Atlas of Living Australia.  To change your species names, we will again use ``pandas`` to do 
this, as ``pandas`` has the built-in function ``replace``.  The first example is for single-name replacement, and 
the second one is writing a loop for changing all species names at once.

.. prompt:: python

    >>> # example single change
    >>> my_dwca.occurrences['scientificName'] = self.occurrences['scientificName'].replace(regex="Acacia murayana", value="Acacia murrayana")
    >>> 
    >>> # example multiple changes
    >>> name_changes = {
    ...     "Eucalyptus camaldulensis var. obtusa": "Eucalyptus camaldulensis subsp. obtusa",
    ...     "Acacia murayana": "Acacia murrayana",
    ...     "Eucalyptus sclerophylla": "Eucalyptus racemosa"
    ... }
    >>> for name in name_changes:
    ...     my_dwca.occurrences['scientificName'] = self.occurrences['scientificName'].replace(regex=name, value=name_changes[name])
    ... 
    >>> my_dwca.occurrences

.. program-output:: python -W ignore galaxias_user_guide/preparing_eventcore_script.py 10

To add higher level taxonomy according to the chosen backbone, see `here <add_higher_taxon.html>`_