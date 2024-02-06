:orphan:

Preparing Your Metadata
===============================

*To follow along with these steps using cleaned example data, download it* :download:`here <data_clean.csv>`

*Note: For exercises involving editing markdowns and making the* ``eml.xml`` *, you do 
not have to have your data processed.  However, for the exercise genearting the* 
``meta.xml`` *, you will need your data to be Darwin-Core compliant.  If you have not 
done this yet, follow the instructions in* [Preparing Your Data](../preparing_data.html)

To build a Darwin Core Archive, you will not only need the data, but your metadata in 
the correct format to submit it to one of the Living Atlases.  This metadata comes in 
two portions: the ``eml.xml`` and the ``meta.xml``.  

Ideally, you will generate your metadata in the following way:

- Getting Your Markdown
- Editing Your Markdown
- Generate Your Metadata (``eml.xml``)
- Generate Your Darwin Core Descriptor (``meta.xml``)

.. grid:: 1 2 2 2
    :gutter: 4

    .. grid-item-card:: 
        :link: preparing_metadata/get_markdown.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Getting Your Markdown** 

    .. grid-item-card::
        :link: preparing_metadata/edit_markdown.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Editing Your Markdown**

    .. grid-item-card:: 
        :link: preparing_metadata/generate_eml_xml.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg
                
        **Generating Your Metadata** 

    .. grid-item-card::
        :link: preparing_metadata/generate_meta_xml.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: ../../source/_static/icons/user_guide.svg

        **Make Darwin Core Descriptor**