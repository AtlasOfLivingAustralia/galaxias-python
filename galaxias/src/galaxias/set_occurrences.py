import corella

def set_occurrences(occurrences=None,
                    occurrenceID=None,
                    catalogNumber=None,
                    recordNumber=None,
                    basisOfRecord=None,
                    occurrenceStatus=None,
                    sep='-',
                    events=None,
                    add_eventID=False,
                    eventType=None):
    """
    Checks for unique identifiers of each occurrence and how the occurrence was recorded.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        occurrenceID: ``str`` or ``bool``
            Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
            provided, the column will be renamed.  If ``True`` is provided, unique identifiers
            will be generated in the dataset.
        catalogNumber: ``str`` or ``bool``
            Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
            provided, the column will be renamed.  If ``True`` is provided, unique identifiers
            will be generated in the dataset.
        recordNumber: ``str`` or ``bool``
            Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
            provided, the column will be renamed.  If ``True`` is provided, unique identifiers
            will be generated in the dataset.
        sep: ``char``
            Separation character for composite IDs.  Default is ``-``.
        basisOfRecord: ``str``
            Either a column name (``str``) or a valid value for ``basisOfRecord`` to add to 
            the dataset.
        occurrenceStatus: ``str``
            Either a column name (``str``) or a valid value for ``occurrenceStatus`` to add to 
            the dataset.
        add_eventID: ``logic``
            Either a column name (``str``) or a valid value for ``occurrenceStatus`` to add to 
            the dataset.
        events: ``pd.DataFrame``
            Dataframe containing your events.
        eventType: ``str``
            Either a column name (``str``) or a valid value for ``eventType`` to add to 
            the dataset.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        `Standardising Occurrences <../../html/galaxias_user_guide/occurrences/index.html>`_
    """
    return corella.set_occurrences(occurrences=occurrences,occurrenceID=occurrenceID,sep=sep,
                                   catalogNumber=catalogNumber,recordNumber=recordNumber,
                                   basisOfRecord=basisOfRecord,occurrenceStatus=occurrenceStatus,
                                   add_eventID=add_eventID,events=events,eventType=eventType)