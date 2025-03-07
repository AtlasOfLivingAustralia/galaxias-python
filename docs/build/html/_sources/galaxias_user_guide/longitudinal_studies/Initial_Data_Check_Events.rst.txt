.. _Initial_Data_Check_Events:

Initial Data Check Events
======================================

When you're ready to start submitting your data, there are a number of things to 
check to ensure the ingestion process into the ALA is smooth.  Some of this is ensuring 
that your column names conform to Darwin Core Vocabulary standards, and that your 
data is in the correct format (i.e. numerical columns are actually numerical).  

*Note: the 

For these examples, we will be using the the dataset linked in the homepage.  If, however, you want to 
go through this workflow using your own data, please feel free to do so!  

To read in the data you want to use, you're going to use ``pandas`` to read in the csv file as a table.

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> occ = pd.read_csv('<NAME_OF_OCCURRENCES>.csv')
    >>> events = pd.read_csv('<NAME_OF_EVENTS>.csv')
    >>> my_dwca.check_data(occurrences=occ,
    ...                    events=events)

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 1

For our initial data example, the data tests may not be showing any errors, but 
unfortunately, this means no column names were checked.  This is because the names 
of the columns are not part of the standard Darwin Core Vocabulary.  Thankfully, 
we have created a series of functions that can help you get your data into the 
Darwin Core standard.  To show the functions ``corella`` contains that can help you 
do this, we have developed an all-purpose function called ``suggest_workflow()``.  Here 
are the results of this particular dataset:  

.. prompt:: python

    >>> my_dwca.suggest_workflow(occurrences=occ,
    ...                          events=events)

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 2

To learn more about how to use these functions, go to 

- `use_events <use_events.html>`_
- `use_datetime <use_datetime.html>`_