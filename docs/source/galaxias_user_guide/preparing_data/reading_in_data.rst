:orphan:

Reading your data into a ``dwca`` object
------------------------------------------------------

Before you do any kind of data preparation, you need to read your data (in ``csv`` format) into a ``galaxias dwca`` 
object.  This will consist of creating a ``pandas data frame`` object, then adding it to a ``dwca`` object.

.. prompt:: python

    >>> import galaxias
    >>> import pandas as pd
    >>> my_dwca = galaxias.dwca(occurrences="occurrences.csv")

If you have events along with occurrences, you then do this:

.. prompt:: python

    >>> import galaxias
    >>> import pandas as pd
    >>> my_dwca = galaxias.dwca(occurrences="occurrences.csv",events="events.csv")


Go to `Next: Renaming Columns <rename_columns_to_dwca.html>`_