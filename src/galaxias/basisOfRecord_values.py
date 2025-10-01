import pandas as pd

def basisOfRecord_values():
    """
    A ``pandas.Series`` of accepted (but not mandatory) values for ``basisOfRecord`` values.

    Parameters
    ----------
        None

    Returns
    -------
        A ``pandas.Series`` of accepted (but not mandatory) values for ``basisOfRecord`` values..
    
    Examples
    --------

    .. prompt:: python

        >>> galaxias.basisOfRecord_values()

    .. program-output:: python -c "import galaxias;print(galaxias.basisOfRecord_values())"
    """
    return pd.DataFrame({'basisOfRecord values': ["humanObservation",
                                                  "machineObservation",
                                                  "livingSpecimen",
                                                  "preservedSpecimen",
                                                  "fossilSpecimen",
                                                  "materialCitation"]})
