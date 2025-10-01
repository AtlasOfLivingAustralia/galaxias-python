import corella

def countryCode_values():
    """
    A ``pandas.Series`` of accepted (but not mandatory) values for ``countryCode`` values.

    Parameters
    ----------
        None

    Returns
    -------
        A ``pandas.Series`` of accepted (but not mandatory) values for ``countryCode`` values..
    
    Examples
    --------

    .. prompt:: python

        >>> galaxias.countryCode_values()

    .. program-output:: python -c "import galaxias;print(galaxias.countryCode_values())"
    """
    return corella.countryCode_values()
