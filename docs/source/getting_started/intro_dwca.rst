:orphan:

What is a Darwin Core Archive?
=================================

According to `Wikipedia <https://en.wikipedia.org/wiki/Darwin_Core_Archive>`_, A Darwin Core Archive (DwC-A) is "a biodiversity 
informatics data standard that makes use of the Darwin Core terms to produce a single, self-contained dataset for species occurrence, 
checklist, sampling event or material sample data."  However, what it actually looks like is a zip file, or zip archive, with 
at least three specifically formatted files:

- ``occurrences.csv``
- ``eml.xml``
- ``meta.xml``

The ``occurrences.csv`` is your species occurrence information.  This contains data like latitude and longitude of occurrence, as 
well as the species.  The column names have to match to specific `Darwin Core Terms <https://dwc.tdwg.org/terms/>`_, and include 
particular information depending on which living atlas you are planning to submit your data to.

The ``eml.xml`` is your dataset metadata, and contains information such as the license associated with the dataset, the author, 
title, how to cite dataset, etc.

The ``meta.xml`` is the Darwin Core Archive descriptor, meaning it describes the information found in the dataset.  This will say 
where the metadata is and the file name (i.e. ``eml.xml``), along with the information included in your ``occurrences.csv`` file.  
This file also includes extension information, such as ``multimedia`` (if you have images, videos or sounds you want to include 
with your dataset), 

Extensions
-------------

- ``multimedia``: this extension is for those who have images, videos or sounds they would like to include in their dataset.
- ``eventCore``: not sure...