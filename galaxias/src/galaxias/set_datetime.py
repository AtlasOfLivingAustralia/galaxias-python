import corella

def set_datetime(dataframe=None,
                 eventDate=None,
                 year=None,
                 month=None,
                 day=None,
                 eventTime=None,
                 string_to_datetime=False,
                 yearfirst=True,
                 dayfirst=False,
                 time_format='mixed'):
    """
    Checks for time information, such as the date an occurrence occurred.  Also runs checks 
    on the validity of the format of the date.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        eventDate: ``str``
            A column name (``str``) denoting the column with the dates of the events, or a ``str`` or 
            ``datetime.datetime`` object denoting the date of the event.
        year: ``str`` or ``int``
            A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
            the year of the event.
        month: ``str`` or ``int``
            A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
            the month of the event.
        day: ``str`` or ``int``
            A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
            the day of the event.
        eventTime: ``str``
            A column name (``str``) denoting the column with the dates of the events, or a ``str`` denoting
            the time of the event.
        string_to_datetime: ``logical``
            An argument that tells ``corella`` to convert dates that are in a string format to a ``datetime`` 
            format.  Default is ``False``.
        yearfirst: ``logical``
            An argument to specify whether or not the day is first when converting your string to datetime.  
            Default is ``True``.
        dayfirst: ``logical``
            An argument to specify whether or not the day is first when converting your string to datetime.  
            Default is ``False``.
        time_format: ``str``
            A ``str`` denoting the original format of the dates that are being converted from a ``str`` to a 
            ``datetime`` object.  Default is ``'mixed'``.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data
    
    Examples
    ----------
        `Standardising Occurrences <../../html/galaxias_user_guide/occurrences/index.html>`_
        `Standardising Events <../../html/galaxias_user_guide/events/index.html>`_
    """
    return corella.set_datetime(dataframe=dataframe,eventDate=eventDate,year=year,month=month,
                                day=day,eventTime=eventTime,string_to_datetime=string_to_datetime,
                                yearfirst=yearfirst,dayfirst=dayfirst,time_format=time_format)