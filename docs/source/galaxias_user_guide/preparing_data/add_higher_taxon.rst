:orphan:

Adding higher order taxonomic information
---------------------------------------------

Once you've ensured all your taxon names are correct, you should add higher order taxonomic information to
ensure that you have the correct taxon.  Thankfully, you can do this with one function in ``galaxias``:

.. prompt:: python

    >>> my_dwca.add_taxonomic_information()
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/preparing_data_script.py add_taxon

``Note``: we have provided the higher taxonomic information we have on the backbone.  It is up to the 
user to confirm they are happy with this taxonomy, or if they spot any errors, 
`contact us <mailto:support@ala.org.au>`_.

If you generate another data report and there are still missing requirements (as with this one), go to 
`our other articles <../preparing_data.html>`_ for more information on how to fill them.