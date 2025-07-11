:orphan:

Longitudinal Studies (Events)
=================================

:download:`Example Events<../data/events_use.csv>`
:download:`Example Occurrences<../data/occurrences_event_nomulti.csv>`

In a research project, data collection can take place at multiple 
locations and times. At each location and time, there are often 
multiple collected samples to capture variation in a study area 
or time-period. In Darwin Core, the data collected from this type 
of project is Event-based.

Events are any action that “occurs at some location during some time.” 
[from TDWG](https://dwc.tdwg.org/list/#dwc_Event). Each sample, for 
example, is a unique event, with its own environmental attributes 
(like topography, tree cover and soil composition) that affect what 
organisms occur there and how likely they are to occur. Observations 
of organisms take place within each Event. As such, Events add hierarchy 
to a dataset by grouping simultaneous observations into groups, as 
opposed to Occurrence-only data which is processed as if all occurrences 
are independent. Event-based data collection adds richness to ecological 
data that can be useful for more advanced modelling techniques.

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