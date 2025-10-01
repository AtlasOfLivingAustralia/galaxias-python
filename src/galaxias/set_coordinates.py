import corella

def set_coordinates(dataframe=None,
                    decimalLatitude=None,
                    decimalLongitude=None,
                    geodeticDatum=None,
                    coordinateUncertaintyInMeters=None,
                    coordinatePrecision=None):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        decimalLatitude: ``str``
            A column name that contains your latitudes (units in degrees).
        decimalLongitude: ``str``
            A column name that contains your longitudes (units in degrees).
        geodeticDatum: ``str`` 
            A column name or a ``str`` with he datum or spatial reference system 
            that coordinates are recorded against (usually "WGS84" or "EPSG:4326"). 
            This is often known as the Coordinate Reference System (CRS). If your 
            coordinates are from a GPS system, your data are already using WGS84.
        coordinateUncertaintyInMeters: ``str``, ``float`` or ``int`` 
            A column name (``str``) or a ``float``/``int`` with the value of the 
            coordinate uncertainty. ``coordinateUncertaintyInMeters`` will typically 
            be around ``30`` (metres) if recorded with a GPS after 2000, or ``100`` 
            before that year.
        coordinatePrecision: ``str``, ``float`` or ``int``
            Either a column name (``str``) or a ``float``/``int`` with the value of the 
            coordinate precision. ``coordinatePrecision`` should be no less than 
            ``0.00001`` if data were collected using GPS.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        `Standardising Occurrences <../../html/galaxias_user_guide/occurrences/index.html>`_
    """
    return corella.set_coordinates(dataframe=dataframe,decimalLatitude=decimalLatitude,
                                   decimalLongitude=decimalLongitude,geodeticDatum=geodeticDatum,
                                   coordinateUncertaintyInMeters=coordinateUncertaintyInMeters,
                                   coordinatePrecision=coordinatePrecision)