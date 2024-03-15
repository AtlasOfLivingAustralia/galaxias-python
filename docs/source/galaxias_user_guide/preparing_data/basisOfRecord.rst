:orphan:

``basisOfRecord``
====================

``basisOfRecord`` refers to how the occurrence was recorded.  This is important for distinguishing individuals 
observed in the wild versus a museum specimen.  This can also include things like camera traps and fossils.  
Here, we show (from the ``galah-python`` package) what options are available:

.. program-output:: python -c "import galah;print(galah.show_values(field='basisOfRecord'))"

If all of the observations you have were observed by a human, you can use the command in the previous page:

.. prompt:: python

    >>> my_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"

This will add a column in the data and flag that all your observations were from humans.

However, if you want to change specific entries (say the first 10 observations are from camera traps), you can 
write a piece of code that creates a column and changes the first 10 observations to ``MACHINE_OBSERVATION``:

.. prompt:: python

    >>> # first, create the column and set the default value
    >>> my_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    >>> 
    >>> # now, loop over the first 10 entries and change 
    >>> for i in range(10):
    ...     my_dwca.occurrences.loc[i,"basisOfRecord"] = "MACHINE_OBSERVATION"
    ... 
    >>> my_dwca.occurrences

Next: `unique identifiers <unique_ids.html>`_