:orphan:

Independent Observations
===================================

:download:`Example Occurrences<../data/occurrences_dwc.csv>`

Data of species observations is referred to as occurrence data. 
In Living Atlases like the Atlas of Living Australia (ALA), this is 
the default type of data stored.

Using occurrence-based datasets assume that all observations are 
independent of each other. The benefit of this assumption is that 
observational data can remain simple in structure - every observation 
is made at a specific place and time. This simplicity allows all 
occurrence-based data to be aggregated and used together.

Below are examples of how to prepare both required and optional 
data for an occurrence dataset.

.. grid:: 1 2 2 2
    :gutter: 4

    .. grid-item:: **Required**

        - :ref:`Initial Data Check`
        - :ref:`set_coordinates`
        - :ref:`set_datetime`
        - :ref:`set_occurrences`
        - :ref:`set_scientific_name`
        - :ref:`What Does A Passing Occurrences Dataset Look Like?`

    .. grid-item:: **Optional**

        - :ref:`convert_coordinates`
        - :ref:`Creating Unique IDs`
        - :ref:`set_abundance`
        - :ref:`set_collection`
        - :ref:`set_individual_traits`
        - :ref:`set_license`
        - :ref:`set_locality`
        - :ref:`set_taxonomy`

.. toctree::
   :maxdepth: 5
   :titlesonly:
   :hidden:

   Initial_Data_Check
   set_coordinates
   set_datetime
   set_occurrences
   set_scientific_name
   convert_coordinates
   creating_unique_IDs
   set_abundance
   set_collection
   set_individual_traits
   set_license
   set_locality
   set_taxonomy
   passing_dataset