import corella

def set_scientific_name(dataframe=None,
                        scientificName=None,
                        taxonRank=None,
                        scientificNameAuthorship=None):
    """
    Checks for the name of the taxon you identified is present.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        scientificName: ``str``
            A column name (``str``) denoting all your scientific names.
        taxonRank: ``str``
            A column name (``str``) denoting the rank of your scientific names (species, genus etc.)
        scientificNameAuthorship: ``str``
            A column name (``str``) denoting who originated the scientific name.

    Returns
    -------
        None - the occurrences dataframe is updated

    Examples
    ----------
        `Standardising Occurrences <../../html/galaxias_user_guide/occurrences/index.html>`_
    """
    return corella.set_scientific_name(dataframe=dataframe,scientificName=scientificName,
                                       taxonRank=taxonRank,scientificNameAuthorship=scientificNameAuthorship)