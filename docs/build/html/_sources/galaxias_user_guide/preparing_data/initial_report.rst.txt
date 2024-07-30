:orphan:

Generating An Initial Report
=======================================

``galaxias`` is set up to check your data to ensure it is compliant with the Darwin Core standard, and specifically 
with the Atlas of Living Australia.  To make this more user-friendly, we have included a function which prints a 
streamlined report, complete with a suggested workflow to follow if there are missing requirements.  To run an initial 
check on your data, run the following:

.. prompt:: Python

    >>> import galaxias
    >>> my_dwca = galaxias.dwca(occurrences="occurrences.csv")
    >>> my_dwca.check_data()

.. program-output:: python -W ignore galaxias_user_guide/preparing_data_script.py 1

Here, we can see how many of our column names correspond with Darwin Core terms, and what data specifically we are missing 
to have a Darwin Core - compliant dataset.

Next: `Adding Occurrence-Specific Terms <use_occurrences.html>`_.