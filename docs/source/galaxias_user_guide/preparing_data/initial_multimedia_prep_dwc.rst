:orphan:

How to Prepare The Required Multimedia options for your ``csv``
====================================================================

*Note: If you instead have an EventCore, go to* `Multimedia EventCore Preparation <initial_multimedia_prep_eventcore.html>`_

To add your multimedia extension to your archive, you will need to create a new csv titled ``multimedia.csv``.  In it, 
you will only need two fields to tie your multimedia to your occurrences:

- ``occurrenceID``

    This is your unique identifier for each occurrence.  Each occurrence may have multiple multimedia files (and therefore 
    the same ``occurrenceID``), but each multimedia file must only have one ``occurrenceID``.

- ``identifier``

    This is the name of or link to the multimedia file.  Each multimedia file must only have one ``occurrenceID``.

So, if you had five occurrences, and you had one image for four occurrences, and two for the last occurrence, your 
multimedia file would look something like this:

.. program-output:: python -W ignore galaxias_user_guide/preparing_data/multimedia_dwc_example.py

Unfortunately, to ensure that your multimedia files are correctly associated with each occurrence, you will need to 
manually check this.  [Is this correct?]

*NOTE: NEED TO DECIDE IF WE WILL ACCEPT MULTIMEDIA AS PART OF THE ARCHIVE OR OTHERS WILL HOST PHOTOS SOMEWHERE*

If you would like to add any recommended terms, such as the type of multimedia, format, title, description etc. see 
`Recommended Multimedia Options <recommended_multimedia_terms_dwc.html>`_.