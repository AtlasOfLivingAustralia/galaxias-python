import corella

def set_abundance(dataframe=None,
                  individualCount=None,
                  organismQuantity=None,
                  organismQuantityType=None):
    """
    One of the functions you can use to check your data is ``set_abundance()``.  
    This function aims to check that you have the following:

    - ``individualCount``: the number of individuals observed of a particular species

    It can also (optionally) can check the following:

    - ``organismQuantity``: a description of your individual counts
    - ``organismQuantityType``: describes what your organismQuantity is

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        individualCount: ``str``
            A column name that contains your individual counts (should be whole numbers).
        organismQuantity: ``str``
            A column name that contains a number or enumeration value for the quantity of organisms.  
            Used together with ``organismQuantityType`` to provide context.
        organismQuantityType: ``str`` 
            A column name or phrase denoting the type of quantification system used for ``organismQuantity``.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.

    Examples
    ----------
        .. prompt:: Python
        
            >>> occ_abundance = galaxias.set_abundance(dataframe=occ,individualCount='count')
    """
    return corella.set_abundance(dataframe=dataframe,individualCount=individualCount,
                                 organismQuantity=organismQuantity,organismQuantityType=organismQuantityType)

