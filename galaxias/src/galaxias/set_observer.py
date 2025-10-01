import corella

def set_observer(dataframe=None,
                 recordedBy=None,
                 recordedByID=None):
    """
    Checks for the name of the taxon you identified is present.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        recordedBy: ``str``
            A column name or name(s) of people, groups, or organizations responsible 
            for recording the original occurrence. The primary collector or observer should be 
            listed first.
        recordedByID: ``str``
            A column name or the globally unique identifier for the person, people, groups, or organizations 
            responsible for recording the original occurrence.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        .. prompt:: Python

            >>> occ_obs = galaxias.set_observer(dataframe=occ,recordedBy='recorder',recordedByID='orcids')
    """
    return corella.set_observer(dataframe=dataframe,recordedBy=recordedBy,recordedByID=recordedByID)