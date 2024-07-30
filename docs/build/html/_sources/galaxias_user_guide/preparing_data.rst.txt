:orphan:

Preparing Your Data for a DwCA
===============================

*To follow along with these steps using example files, download occurrences and/or events here:* 

:download:`occurrences <occurrences_dwc.csv>`

.. :download:`events <events.csv>`
.. :download:`multimedia <multimedia_occ.csv>`

For these exercises, we are assuming your data is currently in a ``csv`` format.  

To build a Darwin Core Archive, your will need to ensure your data is "Darwin Core Compliant".  However, 
this is relatively straightforward!  As you've done the bulk collection of your data, it is likely that 
your data is close to submission already, and will only require a few preparation steps. 

Step-By-Step Preparation of Occurrence Data
---------------------------------------------- 

Something here.

.. grid:: 3
    :gutter: 3

    .. grid-item-card::
        :link: preparing_data/data_directory_creation.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Reading and Storing Your Data**

    .. grid-item-card::
        :link: preparing_data/initial_report.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Generating An Initial Report**

    .. grid-item-card::
        :link: preparing_data/use_occurrences.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Occurrence-Specific Terms**

    .. grid-item-card::
        :link: preparing_data/use_scientific_name.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Checking Scientific Names**

    .. grid-item-card::
        :link: preparing_data/use_coordinates.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Location Data**

    .. grid-item-card::
        :link: preparing_data/use_datetime.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Dates and Times**

    .. grid-item-card::
        :link: preparing_data/additional_geo.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **OPTIONAL: Additional Location Data**

Additional fields
------------------------------------------------

These are terms that aren't required for submission to your chosen atlas, but they are terms that are recommended, as 
they can add extra context and details that will enrich your data and provide a more complete picture of your dataset.

.. grid:: 3
    :gutter: 3

    .. grid-item-card:: 
        :link: preparing_data/cred_taxon_id.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Crediting Taxonomic Identification**  

    .. grid-item-card:: 
        :link: preparing_data/additional_geo.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Additional Location Information**

    .. grid-item-card:: 
        :link: preparing_data/additional_occ.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Additional Occurrence Information**

    .. grid-item-card::
        :link: preparing_data/uncertainty.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Uncertainty**

..       
    Multimedia Extension
    -----------------------------

    If you want to add multimedia, such as images, sounds, or videos, this section will go over how the files are formatted, 
    what is required vs. recommended, and how to ensure your multimedia is correctly represented in the Darwin Core Archive.

    .. grid:: 4
        :gutter: 4

        .. grid-item-card::
            :link: preparing_data/initial_multimedia_prep_dwc.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **How to Prepare Required Multimedia Options**

        .. grid-item-card::
            :link: preparing_data/recommended_multimedia_terms_dwc.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **How to Prepare Recommended Multimedia Options**

        .. grid-item-card::
            :link: preparing_data/validate_multimedia_occurrence.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Validating Multimedia Extension**

    Extended Measurement Or Fact
    -------------------------------------------


    ``UNDER CONSTRUCTION``

    .. grid:: 4
        :gutter: 4

        .. grid-item-card::
            :link: preparing_data/link_id_measurement.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Linking IDs to measurements**

        .. grid-item-card::
            :link: preparing_data/measurement_prep.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **How to format your measurements**

        .. grid-item-card::
            :link: preparing_data/validate_measurements.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Validating measurements**

.. Example of Final Report
.. -----------------------------

.. ``UNDER CONSTRUCTION``

.. This is an example of a passing and failing???? report of ``dwca`` objects.

.. .. grid:: 3
..     :gutter: 3

..     .. grid-item-card::
..         :link: preparing_data/final_report_occurrence_nomulti.html
..         :class-card: sd-text-black
..         :text-align: center

..         .. raw:: html
..             :file: ../../source/_static/icons/user_guide.svg

..         **Occurrence Passing**

..     .. grid-item-card::
..         :link: preparing_data/final_report_event_nomulti.html
..         :class-card: sd-text-black
..         :text-align: center

..         .. raw:: html
..             :file: ../../source/_static/icons/user_guide.svg

..         **Events Passing**

    ..
        .. grid-item-card::
            :link: preparing_data/final_report_occurrence_multi.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Occurrence/Multimedia**



