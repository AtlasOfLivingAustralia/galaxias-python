import corella

def set_events(dataframe=None,
               eventID=None,
               parentEventID=None,
               eventType=None,
               Event=None,
               samplingProtocol=None,
               event_hierarchy=None,
               sep='-'):
    """
    Identify or format columns that contain information about an Event. An "Event" in Darwin Core Standard refers to an action that occurs at a place and time. Examples include:

    - A specimen collecting event
    - A survey or sampling event
    - A camera trap image capture
    - A marine trawl
    - A camera trap deployment event
    - A camera trap burst image event (with many images for one observation)

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            ``pandas.DataFrame`` with your data
        eventID: ``str``, ``logical``
            A column name (``str``) that contains a unique identifier for your event.  Can also be set 
            to ``True`` to generate values.  Parameters for these values can be specified with the arguments 
            ``sequential_id``, ``add_sequential_id``, ``composite_id``, ``sep`` and ``random_id``
        sep: ``char``
            Separation character for composite IDs.  Default is ``-``.
        parentEventID: ``str``
            A column name (``str``) that contains a unique ID belonging to an event below 
            it in the event hierarchy.
        eventType: ``str`` 
            A column name (``str``) or a ``str`` denoting what type of event you have.
        Event: ``str`` 
            A column name (``str``) or a ``str`` denoting the name of the event.
        samplingProtocol: ``str`` or 
            Either a column name (``str``) or a ``str`` denoting how you collected the data, 
            i.e. "Human Observation".
        event_hierarchy: ``dict``
            A dictionary containing a hierarchy of all events so they can be linked.  For example, 
            if you have a set of observations that were taken at a particular site, you can use the 
            dict {1: "Site Visit", 2: "Sample", 3: "Observation"}.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data

    Examples
    ----------
        `Standardising Events <../../html/galaxias_user_guide/events/index.html>`_
    """
    if event_hierarchy is not None and eventID is None:
        print('setting your eventIDs to a random UUID.  To make a custom eventID, provide column names, and/or the words \'random\', \'sequential\'.')
        eventID='random'
    return corella.set_events(dataframe=dataframe,eventID=eventID,parentEventID=parentEventID,
                              eventType=eventType,Event=Event,samplingProtocol=samplingProtocol,
                              event_hierarchy=event_hierarchy,sep=sep)