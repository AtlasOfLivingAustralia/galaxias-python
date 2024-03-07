:orphan:

Crediting Taxonomic Identification
====================================

Sometimes identification of a species can be tricky for a variety of reasons.  Luckily, 
there are Darwin Core terms users can employ to express their doubts about identification, 
credit a team in the identification of a species, or even list individuals' ORCIDs for 
disambiguation (say someone has a very common name - the ORCID will be a unique ID for 
this person).

``identificationQualifier``
--------------------------------

This term is used when a user has doubts about their assigned taxon.

``identificationReferences``
--------------------------------

These are references the determiner used for identification, and is a good idea when 
there is a particularly difficult identification and the determiner wants to provide 
insight on their identification process.

``identificationVerificationStatus``
----------------------------------------

This category is for indicating how correct taxonomic identification is.  A user will 
provide an integer, which will determine the category of X.

``identifiedBy``
---------------------

This term is particularly useful for when there is a different person or persons collecting 
the data vs. those who are identifying the species observations.  This term allows the user 
to specify who identified the species in question.

``identifiedByID``
----------------------

This is a list of GUIDs (i.e. ORCIDs) of people who have identified the taxon in the observation.  
This is particularly useful for when someone has a common name, and needs to distinguish themselves 
from other researchers, or even those in similar fields.