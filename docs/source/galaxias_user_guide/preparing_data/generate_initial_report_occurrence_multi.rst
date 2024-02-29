:orphan:

Generating a data report
=========================

First, we will want to know how close our data is to being ready for submission to a living 
atlas.  To do that, we will need to first build a ``dwca`` object with ``galaxias``, and then 
run an initial report.  This report will check dates, requirements for your atlas, whether or 
not your taxon have the correct taxonomy for your chosen taxonomic backbone, and if each of 
your occurrences has a unique identifier.

.. prompt:: python

    >>> import galaxias
    >>> import pandas as pd
    >>> occurrences = pd.read_csv("occurrences.csv")
    >>> multimedia = pd.read_csv("multimedia.csv")
    >>> my_dwca = galaxias.dwca(occurrences=occurrences,multimedia=multimedia)
    >>> my_dwca.generate_data_report()

.. program-output:: python -W ignore galaxias_user_guide/multimedia_occurrence_example.py 1