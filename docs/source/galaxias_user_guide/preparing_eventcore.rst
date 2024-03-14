:orphan:

Preparing Your Data for an EventCore
=======================================

*To follow along with these steps using example data, download them using the following links:* 

:download:`events <events.csv>`
:download:`occurrences <occurrences_event_multi.csv>`

For these exercises, we are assuming your data is currently in a ``csv`` format.  

To build an EventCore Archive, your will need to ensure your data has a particular naming convention and 
is in a particular format.  However, this is relatively straightforward!  As you've done the bulk collection 
of your data, it is likely that your data is close to submission already, and will only require a few steps 
to ready it. 

Note about Errors
----------------------

Though you may get a lot of errors in the beginning, most of these errors will likely be attributed to the following:

- Names of columns are not Darwin Core terms
- Taxonomy does not match your chosen backbone

Initial Preparation
-----------------------------

These steps are showing you how to generate a "report", which will tell you what needs to be edited before your data 
can be submitted to your chosen atlas.  It also shows you how to rename columns, as your data won't be checked if the 
column name is not a Darwin Core term.  

.. grid:: 4
    :gutter: 4

    .. grid-item-card:: 
        :link: preparing_data/generate_initial_report_event.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Example Report** 

    .. grid-item-card::
        :link: preparing_data/rename_eventcore_columns.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Renaming All Columns to Event Core**

    .. 
        ..  grid-item-card:: 
            :link: preparing_data/generate_initial_report_event_multi_emof.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg
                    
            **Example Report + Extensions**|

Validating Required Terms
-------------------------------------------

*For information on how to prepare occurrence data, visit* 
`Preparing Occurrences <preparing_occurrence_data.html>`_

These vignettes are for the ``events`` part of the EventCore Archive.

.. grid:: 4
    :gutter: 4

    .. grid-item-card::
        :link: preparing_data/add_req_columns_values_event.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Required Columns and Values**

    .. grid-item-card::
        :link: preparing_data/convert_datetime.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Converting Datetime Formats**

    .. grid-item-card::
        :link: preparing_data/convert_datetime.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Event stuff here???**

Validating Recommended EventCore Terms
-------------------------------------------

``UNDER CONSTRUCTION``

.. grid:: 4
    :gutter: 4

    .. grid-item-card::
        :link: preparing_data/event_core_terms.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Required Event Core Terms**

    .. grid-item-card::
        :link: preparing_data/preparing_event_core.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Preparing An Event Core**

.. 
    Multimedia Extension
    -------------------------------------------

    .. grid:: 4
        :gutter: 4

        .. grid-item-card::
            :link: preparing_data/initial_multimedia_prep_eventcore.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Preparing Required Data for Multimedia**

        .. grid-item-card::
            :link: preparing_data/recommended_multimedia_terms_eventcore.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Preparing Recommended Data for Multimedia**



