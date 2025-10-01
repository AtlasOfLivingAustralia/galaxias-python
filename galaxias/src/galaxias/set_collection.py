import corella

def set_collection(dataframe=None,
                   datasetID=None,
                   datasetName=None,
                   catalogNumber=None):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        datasetID: ``str``
            A column name or other string denoting the identifier for the set of data. May be a global unique 
            identifier or an identifier specific to a collection or institution.
        datasetName: ``str``
            A column name or other string identifying the data set from which the record was derived.
        catalogNumber: ``str`` 
            A column name or other string denoting a unique identifier for the record within the data set or collection.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        .. prompt:: Python
        
            >>> occ_coll = galaxias.set_collection(dataframe=occ,datasetID='id')
    """
    return corella.set_collection(dataframe=dataframe,datasetID=datasetID,
                                  datasetName=datasetName,catalogNumber=catalogNumber)

