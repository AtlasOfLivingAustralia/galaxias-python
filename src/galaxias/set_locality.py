import corella

def set_locality(dataframe=None,
                 continent = None,
                 country = None,
                 countryCode = None,
                 stateProvince = None,
                 locality = None):
    """
    Checks for additional location information, such as country and countryCode.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        continent: ``str``
            Either a column name (``str``) or a string denoting one of the seven continents.
        country: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the country.
        countryCode: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the countryCode.
        stateProvince: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the state or province.
        locality: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the locality.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        .. prompt:: Python

            >>> occ_loc = galaxias.set_locality(dataframe=occ,continent='Oceania',country='Australia')
    """
    
    return corella.set_locality(dataframe=dataframe,continent=continent,
                                country=country,countryCode=countryCode,
                                stateProvince=stateProvince,locality=locality)