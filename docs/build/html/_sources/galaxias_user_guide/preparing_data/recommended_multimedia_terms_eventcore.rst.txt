:orphan:

How to Prepare The Recommended Multimedia options for your ``csv``
====================================================================

*Note: If you don't have any events, go to* `Multimedia Darwin Core Preparation <initial_multimedia_prep_dwc.html>`_

``eventID``, ``occurrenceID`` and ``identifier`` are the required terms you need for your ``multimedia.csv``.  However, if you 
would like to include more information about your images, below are recommended fields.

Additional details
----------------------

- ``type``	

    This is the type of data you are giving in your dataset, such as ``Stillimage`` or ``Sound``.

- ``format``	

    This is more specific than the field ``type``, in that it contains the type of data and the format, i.e. 
    ``image/jpeg`` or ``image/png``.

- ``references``	

    This could be referring to such things as the occurrence record (?)

- ``title``	

    Title of your image.

- ``description``	

    Description of your image.

Creation
-------------

- ``created``	

    The date, in the format ``YYYY-MM-DD`` the multimedia was created.

- ``creator``

    Who created the multimedia.  This field is particularly useful when someone involved in collecting the data is 
    in the author list, but only certain multimedia and/or occurrences are attributed to them.

Usage
-----------

- ``license``

    The license that denotes how others can use your data.