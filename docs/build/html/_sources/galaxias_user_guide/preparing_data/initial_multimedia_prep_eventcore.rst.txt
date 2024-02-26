:orphan:

How to Prepare The Required Multimedia options for your ``csv``
====================================================================

*Note: If you don't have any events, go to* `Multimedia Darwin Core Preparation <initial_multimedia_prep_dwc.html>`_

To add your multimedia extension to your archive, you will need to create a new csv titled ``multimedia.csv``.  In it, 
you will only need two fields to tie your multimedia to your occurrences:

- ``eventID``

    This is your unique identifier for each event.  This eventID may have multiple occurrences and multiple 
    media files, but each occurrence and identifier must only have one ``eventID``.

- ``occurrenceID``

    This is your unique identifier for each occurrence.  Each occurrence may have multiple multimedia files (and therefore 
    the same ``occurrenceID``), but each multimedia file must only have one ``occurrenceID`` and only one ``eventID``.

- ``identifier``

    This is the name of or link to the multimedia file.  Each multimedia file must only have one ``occurrenceID`` and 
    only one ``eventID``.

So, if you had five occurrences, and you had one image for four occurrences, and two for the last occurrence, your 
multimedia file would look something like this:

.. program-output:: python -W ignore galaxias_user_guide/preparing_data/multimedia_eventcore_example.py

Unfortunately, to ensure that your multimedia files are correctly associated with each occurrence, you will need to 
manually check this.  [Is this correct?]

Once you have 

*NOTE: NEED TO DECIDE IF WE WILL ACCEPT MULTIMEDIA AS PART OF THE ARCHIVE OR OTHERS WILL HOST PHOTOS SOMEWHERE*

If you would like to add any recommended terms, such as the type of multimedia, format, title, description etc. see 
`Recommended Multimedia Options <recommended_multimedia_terms_dwc.html>`_.