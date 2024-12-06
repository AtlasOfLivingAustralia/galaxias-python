.. _Introduction:

Introduction
==============

``galaxias`` is a package for collating prepared biodiversity data into Darwin Core Archives 
for submission to the Atlas of Living Australia.  This package assumes you have used our sister 
packages to prepare the following different parts of the Darwin Core Archive:

- ``corella``: this package will help you reformat your data to be in the Darwin Core standard `website here <corella.ala.org.au/Python>`_
- ``paperbark``: this package will help you write and format your metadata by converting a readable markdown file into a metadata xml file (``eml.xml``) `website here <paperbark.ala.org.au/Python>`_

``galaxias`` will then take these files and use them to generate another metadata file, which will 
describe your Darwin Core Archive.  It will then put all of this data into a Darwin Core Archive, 
which you can submit to the Atlas of Living Australia.