import corella

def set_license(dataframe=None,
                license=None,
                rightsHolder=None,
                accessRights=None):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        license: ``str``
            A column name or value denoting a legal document giving official 
            permission to do something with the resource. Must be provided as a 
            url to a valid license.
        rightsHolder: ``str``
            A column name or value denoting the person or organisation owning or 
            managing rights to resource.
        accessRights: ``str``
            A column name or value denoting any access or restrictions based on 
            privacy or security.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        .. prompt:: Python

            >>> occ_lic = galaxias.set_license(dataframe=occ,license=['CC-BY 4.0 (Int)', 'CC-BY-NC 4.0 (Int)'],
            ...                                rightsHolder='The Regents of the University of California',
            ...                                accessRights=['','not-for-profit use only'])
    """
    return corella.set_license(dataframe=dataframe,license=license,rightsHolder=rightsHolder,
                               accessRights=accessRights)