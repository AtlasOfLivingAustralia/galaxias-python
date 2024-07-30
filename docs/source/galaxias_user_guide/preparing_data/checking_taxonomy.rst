:orphan:

Checking taxonomy
--------------------------------

Now that we have renamed the data columns, let's check how our taxonomy compares with the ALA backbone.  To start,
let's generate another data report to see how renaming our columns changes the report.

.. prompt:: python

    >>> my_dwca.generate_data_report()

# .. program-output:: python galaxias_user_guide/preparing_data_script.py check_taxon1

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

# .. program-output:: python galaxias_user_guide/preparing_data_script.py check_taxon

Adding higher order taxonomic information
---------------------------------------------

Once you've ensured all your taxon names are correct, you should add higher order taxonomic information to
ensure that you have the correct taxon.  Thankfully, you can do this with one function in ``galaxias``:

.. prompt:: python

    >>> my_dwca.add_taxonomic_information()
    >>> my_dwca.occurrences.head()

# .. program-output:: python galaxias_user_guide/preparing_data_script.py add_taxon

``Note``: we have provided the higher taxonomic information we have on the backbone.  It is up to the 
user to confirm they are happy with this taxonomy, or if they spot any errors, 
`contact us <mailto:support@ala.org.au>`_.

If you generate another data report and there are still missing requirements (as with this one), go to 
`our other articles <../preparing_data.html>`_ for more information on how to fill them.