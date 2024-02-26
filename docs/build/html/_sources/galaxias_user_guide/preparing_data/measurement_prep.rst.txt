:orphan:

Formatting measurements for EventCore
======================================

In the article about ``Linking IDs with measurements``, we covered 

For each measurement, there needs to be descriptions of the following:

- How can I uniquely identify this specific measurement? (``measurementID``)
- What type of measurement is it? (``measurementType``)
- What is the value of the measurement? (``measurementValue``)
- What units am I using for the measurement? (``measurementUnit``)
- How accurate are my measurements? (``measurementAccuracy``)

Required Terms
-------------------

``measurementID`` :	
A unique identifier for the measurement, which may be a Globally Unique Identifier or it may be an identifier 
specific to the dataset.  An analogous example is ``eventID`` or ``occurrenceID``.

``measurementType`` :
A text description of the property being measured or the type of assertion being made. For example: 
“water acidity”, “vegetation” or “wing span”. 

``measurementValue`` :
The result of the measurement or the fact being asserted. For example, if we were using the 
``measurementType`` listed above: “6.9”, “myrtle-beech” or “10”.

``measurementUnit`` :	
The unit of measurement, for example: “pH” or “cm”. Assertions of fact, such as X, have no unit.

``measurementAccuracy`` :	
A statement of how accurate your measurement is, usually in the form of a plus/minus value. For example, 
if you were taking a pH measurement and your pH meter had an error of 0.01 pH units, you would put "0.01" in 
this column.

Optional Terms
------------------

``measurementDeterminedDate`` :	
The date (and time) the measurement or fact was taken. If this is absent, the ``eventDate`` will be used instead.

``measurementDeterminedBy`` :	
The name of the person, group or organisation that determined the measurement or fact.  This is important to include 
if there were multiple people taking the measurements, and you want to delineate who took each measurement.

``measurementRemarks`` :	
Additional comments or remarks accompanying the measurement or fact.  For example, if there are caveats or extra notes 
about the measurement, this is where you would include them.

Example dataset
-----------------------

.. program-output:: python -W ignore galaxias_user_guide/preparing_data/measurement_example.py