import corella

def set_individual_traits(dataframe=None,
                          individualID=None,
                          lifeStage=None,
                          sex=None,
                          vitality=None,
                          reproductiveCondition=None):
    
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        individualID: ``str``
            A column name containing an identifier for an individual or named group of 
            individual organisms represented in the Occurrence. Meant to accommodate 
            resampling of the same individual or group for monitoring purposes. May be 
            a global unique identifier or an identifier specific to a data set.
        lifeStage: ``str``
            A column name containing the age, class or life stage of an organism at the time of occurrence.
        sex: ``str`` 
            A column name or value denoting the sex of the biological individual.
        vitality: ``str``
            A column name or value denoting whether an organism was alive or dead at the time of collection or observation.
        reproductiveCondition: ``str``
            A column name or value denoting the reproductive condition of the biological individual.
        
    Returns
    -------
        None - the occurrences dataframe is updated

    Examples
    ----------
        .. prompt:: Python

            >>> occ_traits = galaxias..set_individual_traits(dataframe=occ,individualID=['123456','123457'],
            ...                                              lifeStage='adult',sex=['male','female'],
            ...                                              vitality='alive',reproductiveCondition='not reproductive')
    """
    return corella.set_individual_traits(dataframe=dataframe,individualID=individualID,
                                         lifeStage=lifeStage,sex=sex,vitality=vitality,
                                         reproductiveCondition=reproductiveCondition)