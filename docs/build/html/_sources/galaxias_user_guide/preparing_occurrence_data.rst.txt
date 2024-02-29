:orphan:

Preparing Your Data for a DwCA
===============================

*To follow along with these steps using example occurrence data, download it* :download:`here <occurrences_dwc.csv>`

*To follow along with these steps using both occurrence and example multimedia data, download the multimedia file* :download:`here <multimedia_occ.csv>`

For these exercises, we are assuming your data is currently in a ``csv`` format.  

To build a Darwin Core Archive, your data needs to have specific columns and be in specific formats 
for it to be accepted to a living atlas.   A list of required and recommended values are on [AMANDA 
ADD LINK HERE], along with their definitions and examples.  The "Initial Preparation" covers this, 
and must be done before you start validating your data against Darwin Core standards and the requirements 
of your chosen living atlas.

"Validating Data Against DwC Standards" is a series of articles that can be done in any order (though it 
is a good idea to check your taxonomy before adding higher order taxonomy).  It is also a good idea to 
generate a data report after completing one of the steps in this section, to make sure everything went as 
planned.

Initial Preparation
-----------------------------

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
        :link: preparing_data/generate_initial_report_occurrence_multi.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Data Report with Multimedia**

    .. grid-item-card::
        :link: preparing_data/rename_columns_to_dwca.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Renaming Columns to Darwin Core**

Validating Required Darwin Core Standards
------------------------------------------------

.. grid:: 5
    :gutter: 4

    .. grid-item-card:: 
        :link: preparing_data/checking_taxonomy.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Check Taxonomy** 

    .. grid-item-card::
        :link: preparing_data/add_higher_taxon.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Add Higher Order Taxonomy**

    .. grid-item-card::
        :link: preparing_data/add_req_columns_values.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Adding Required Columns and Values**

    .. grid-item-card::
        :link: preparing_data/convert_coordinates.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Converting Spatial Coordinates**

    .. grid-item-card::
        :link: preparing_data/convert_datetime.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Converting Datetime Formats**

Validating Recommended Darwin Core Standards
------------------------------------------------

.. grid:: 5
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
                
        **Rest**
        
Multimedia Extension
-----------------------------

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

.. grid:: 4
    :gutter: 4

    .. grid-item-card::
        :link: preparing_data/final_report_occurrence_nomulti.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Final Example Report of Passing Occurrence Data**

    .. grid-item-card::
        :link: preparing_data/final_report_occurrence_multi.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Final Example Report of Passing Occurrence/Multimedia Data**