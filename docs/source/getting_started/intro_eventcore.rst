:orphan:

What is an Event Core Archive?
=================================

Before we go into what an Event Core Archive is, we will first define what an "event" is in this context.

For our purposes, an 'Event' is an entity that holds the key information about activities that lead to a 
species occurrence.  Examples are regular surveys, multiple visits to specific sites, seed germination trials, 
etc.  

There are a few key indicators that you would want to use the Event Core system over the usual Darwin Core system:

- You have data on surveys, site-specific data etc.
- Know how the data was collected and this information is structured
- Have abiotic measurements relevant to your occurrence records, such as temperature


How is an Event Core structured?
-----------------------------------

An Event Core is different than a regular Darwin Core Archive, in that the core of this archive are the recorded 
events.  The big question is: how does all the information relate to one another?

Below is an example of what kinds of events make up an Event core.  It also contains information on how you can 
record data that has site-level information, as well as X.

.. image:: Slide2.png

What does an Event Core look like in practice?
--------------------------------------------------

Your data file will consist of four required files:

- ``meta.xml``
- ``eml.xml``
- ``events.csv``
- ``occurrences.csv``

and two optional files:

- ``multimedia.csv``
- ``extendedMeasurementOrFact.csv``

The files will look like this:

.. image:: Slide1.png