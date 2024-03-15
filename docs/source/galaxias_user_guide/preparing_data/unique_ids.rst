:orphan:

Unique Identifiers
=====================

Every occurrence must have a unique identifier to go with it.  You have a choice of one or more unique identifiers 
present in the Darwin Core vocabulary:

- ``occurrenceID``: An identifier for the dwc:Occurrence (as opposed to a particular digital record of the dwc:Occurrence). In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the dwc:occurrenceID globally unique.
- ``catalogNumber``: An identifier (preferably unique) for the record within the data set or collection.
- ``recordNumber``: An identifier given to the dwc:Occurrence at the time it was recorded. Often serves as a link between field notes and a dwc:Occurrence record, such as a specimen collector's number.

Luckily, the ``dwca`` object has a function which will create UUID (Unique Identifiers) for each of your occurrences, should you 

.. prompt:: python

    >>> my_dwca.add_unique_occurrence_IDs(column_name="occurrenceID")
    >>> my_dwca.occurrences.head()

Next, go to `coordinates <convert_coordinates.html>`_.