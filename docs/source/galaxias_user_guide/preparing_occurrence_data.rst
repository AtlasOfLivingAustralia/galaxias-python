:orphan:

Preparing Your Data for a DwCA
===============================

*To follow along with these steps using example files, download them here:* 

:download:`occurrences <occurrences_dwc.csv>`

.. :download:`multimedia <multimedia_occ.csv>`

For these exercises, we are assuming your data is currently in a ``csv`` format.  

To build a Darwin Core Archive, your will need to ensure your data has a particular naming convention and 
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
        :link: preparing_data/generate_initial_report_occurrence.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Generate Data Report** 

    .. grid-item-card::
        :link: preparing_data/rename_columns_to_dwca.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Renaming Columns to Darwin Core**

    .. 
        .. grid-item-card::
            :link: preparing_data/generate_initial_report_occurrence_multi.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Data Report with Multimedia**


Validating Required Occurrence Data
------------------------------------------------

This is a series of articles that can be done in any order (the lone exception being you need to check your species names 
against the taxonomic backbone of your atlas before adding higher order taxonomy).  It is also a good idea to 
generate a data report after completing one of the steps in this section, to ensure you catch any niggling errors.

.. grid:: 4
    :gutter: 4

    .. grid-item-card:: 
        :link: preparing_data/checking_taxonomy.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Taxonomy** 

    .. grid-item-card::
        :link: preparing_data/add_req_columns_values.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Columns**

    .. grid-item-card::
        :link: preparing_data/convert_coordinates.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Lat/Long**

    .. grid-item-card::
        :link: preparing_data/convert_datetime.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Datetime**

Validating Recommended Darwin Core Standards
------------------------------------------------

These are terms that aren't required for submission to your chosen atlas, but they are terms that are recommended, as 
they can add extra context and details that will enrich your data and provide a more complete picture of your dataset.

.. grid:: 4
    :gutter: 4

    .. grid-item-card:: 
        :link: preparing_data/data_obfuscation.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Obscuring Your Data** 

    .. grid-item-card:: 
        :link: preparing_data/cred_taxon_id.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Crediting Taxonomic Identification**  

    .. grid-item-card:: 
        :link: preparing_data/recommended_terms_dumping_ground.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Other**

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

Example of Final Report
-----------------------------

This is an example of a passing report of ``dwca`` objects.

.. grid:: 4
    :gutter: 4

    .. grid-item-card::
        :link: preparing_data/final_report_occurrence_nomulti.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Occurrence**

    ..
        .. grid-item-card::
            :link: preparing_data/final_report_occurrence_multi.html
            :class-card: sd-text-black
            :text-align: center

            .. raw:: html
                :file: ../../source/_static/icons/user_guide.svg

            **Occurrence/Multimedia**