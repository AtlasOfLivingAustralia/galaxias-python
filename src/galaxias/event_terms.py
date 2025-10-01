import corella

def event_terms():
    """
    A ``pandas.Series`` of accepted (but not mandatory) values for event data.

    Parameters
    ----------
        None

    Returns
    -------
        A ``pandas.Series`` of accepted (but not mandatory) values for event data.
    
    Examples
    --------

    .. prompt:: python

        >>> galaxias.event_terms()

    .. program-output:: python -c "import galaxias;print(galaxias.event_terms())"
    """
    return corella.event_terms()
