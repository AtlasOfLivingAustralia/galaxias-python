:orphan:

Events
===================

Example Data: 
:download:`Example Events<../data/events_use.csv>`
:download:`Example Occurrences<../data/occurrences_event_nomulti.csv>`

These are all the functions an explanation for your ``events.txt`` file.  For how to structure 
your ``occurrences.txt`` file, go `here <../independent_observations/index.html>`_.

Before Processing Data
------------------------

- :ref:`How_to_Structure_Events`

Formatting Events 
-------------------------

.. grid:: 1 2 2 2
    :gutter: 4

    .. grid-item:: **Required**

         - :ref:`Initial_Data_Check_Events`
         - :ref:`set_events`
         - :ref:`set_datetime`
         - :ref:`adding_eventID_occurrences`

    .. grid-item:: **Optional**

        - :ref:`set_abundance_events`
        - :ref:`set_locality_events`

Example of Passing Dataset 
----------------------------

- :ref:`What Does A Passing Events Dataset Look Like?`

.. toctree::
   :maxdepth: 5
   :titlesonly:
   :hidden:

   How_to_Structure_Events
   Initial_Data_Check_Events
   set_events
   set_datetime
   adding_eventID_occurrences
   set_abundance_events
   set_locality_events
   passing_dataset