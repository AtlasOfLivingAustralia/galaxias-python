import corella

def set_taxonomy(dataframe=None,
                 kingdom=None,
                 phylum=None,
                 taxon_class=None, 
                 order=None,
                 family=None,
                 genus=None,
                 specificEpithet=None,
                 vernacularName=None):
    """
    Adds extra taxonomic information.  Also runs checks on whether or not the names are the 
    correct data type.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        kingdom: ``str``,``list``
            A column name, kingdom name (``str``) or list of kingdom names (``list``).
        phylum: ``str``,``list``
            A column name, phylum name (``str``) or list of phylum names (``list``).
        taxon_class: ``str``,``list``
            A column name, class name (``str``) or list of class names (``list``).
        order: ``str``,``list``
            A column name, order name (``str``) or list of order names (``list``).
        family: ``str``,``list``
            A column name, family name (``str``) or list of family names (``list``).
        genus: ``str``,``list``
            A column name, genus name (``str``) or list of genus names (``list``).
        specificEpithet: ``str``,``list``
            A column name, specificEpithet name (``str``) or list of specificEpithet names (``list``).
            **Note**: If ``scientificName`` is *Abies concolor*, the ``specificEpithet`` is *concolor*.
        vernacularName: ``str``,``list``
            A column name, vernacularName name (``str``) or list of vernacularName names (``list``).

    Returns
    -------
        None - the occurrences dataframe is updated

    Examples
    ----------
        .. prompt:: Python

            >>> occ_tax = galaxias.set_taxonomy(dataframe=occ,kingdom='Animalia',phylum='Chordata',taxon_class='Aves',
            ...                                 order='Psittaciformes',family='Cacatuidae',genus='Eolophus',
            ...                                 specificEpithet='roseicapilla',vernacularName='Galah')
    """
    return corella.set_taxonomy(dataframe=dataframe,kingdom=kingdom,phylum=phylum,taxon_class=taxon_class,
                                order=order,family=family,genus=genus,specificEpithet=specificEpithet,
                                vernacularName=vernacularName)