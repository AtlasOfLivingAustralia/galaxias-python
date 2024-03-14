:orphan:

Refresher
==============

What workflow am I doing?
----------------------------

See `Workflow <workflow.html>`_.

What is a Darwin Core Archive?
-----------------------------------

According to `Wikipedia <https://en.wikipedia.org/wiki/Darwin_Core_Archive>`_, A Darwin Core Archive (DwC-A) is *"a biodiversity 
informatics data standard that makes use of the Darwin Core terms to produce a single, self-contained dataset for species occurrence, 
checklist, sampling event or material sample data."*  However, what it actually looks like is a zip file, or zip archive.  It will 
have three different pieces of information:

1. Occurrences
2. Metadata about the collection of the data
3. Metadata about the data itself


The ``occurrences.csv`` is your species occurrence information.  This contains data like latitude and longitude of occurrence, as 
well as the species.  The column names have to match to specific `Darwin Core Terms <https://dwc.tdwg.org/terms/>`_, and include 
particular information depending on which living atlas you are planning to submit your data to.

The ``eml.xml`` is your dataset metadata, and contains information such as the license associated with the dataset, the author, 
title, how to cite dataset, etc.

The ``meta.xml`` is the Darwin Core Archive descriptor, meaning it describes the information found in the dataset.  This will say 
where the metadata is and the file name (i.e. ``eml.xml``), along with the information included in your ``occurrences.csv`` file.  
This file also includes extension information, such as ``multimedia`` (if you have images, videos or sounds you want to include 
with your dataset), 

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