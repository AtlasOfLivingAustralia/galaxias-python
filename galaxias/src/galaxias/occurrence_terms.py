import corella

def occurrence_terms():
    """
    A ``pandas.Series`` of accepted (but not mandatory) values for occurrence data.

    Parameters
    ----------
        None

    Returns
    -------
        A ``pandas.Series`` of accepted (but not mandatory) values for occurrence data.
    
    Examples
    --------

    .. prompt:: python

        >>> galaxias.occurrence_terms()

    .. program-output:: python -c "import galaxias;print(galaxias.occurrence_terms())"
    """
    return corella.occurrence_terms()
