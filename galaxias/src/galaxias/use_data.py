import os

def use_data(occurrences=None,
             events=None,
             occurrences_filename='occurrences.csv',
             events_filename='events.csv',
             publishing_dir='./data-publish'):
    """
    Writes occurrence and event files to your publishing directory.

    Parameters
    ----------
        occurrences: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your occurrence data
        events: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your events data
        occurrences_filename: ``str``
            ``str`` containing the desired name for your occurrences file
        events_filename: ``str``
            ``str`` containing the desired name for your events file
        publishing_dir: ``str``
            ``str`` containing the name of your publishing directory

    Returns
    -------
        None - files are written to disk

    Examples
    ----------
        .. prompt:: Python

            >>> galaxias.use_data(occurrences=occ,events=events)
    """
    if not os.path.exists(publishing_dir):
        os.mkdir(publishing_dir)

    if occurrences is None and events is None:
        print('You have not provided any data to write to file, so none will be written.')

    if occurrences is not None:
        occurrences.to_csv('{}/{}'.format(publishing_dir,occurrences_filename),index=False)

    if events is not None:
        events.to_csv('{}/{}'.format(publishing_dir,events_filename),index=False)