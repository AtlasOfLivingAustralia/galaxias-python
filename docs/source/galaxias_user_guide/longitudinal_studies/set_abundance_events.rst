.. _set_abundance_events:

set_abundance
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``set_abundance()``.  
This function aims to check that you have the following:

- ``individualCount``: the number of individuals observed of a particular species

It can also (optionally) can check the following:

- ``organismQuantity``: a description of your individual counts
- ``organismQuantityType``: describes what your organismQuantity is

specifying ``individualCount``
-----------------------------------------

.. prompt:: python

    >>> my_dwca.set_abundance(individualCount='number_birds')
    >>> my_dwca.occurrences.head()

.. program-output:: python galaxias_user_guide/longitudinal_studies/events_workflow.py 14

To learn more about how to use other functions, go to 

- `set_events <set_events.html>`_
- `set_datetime <set_datetime.html>`_

Optional functions:

- `set_locality <set_locality_events.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_