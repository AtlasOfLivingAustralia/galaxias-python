:orphan:

Preparing the DwCA itself 
==========================

Preparing your Darwin Core Archive can be relatively straightforward.  
However, this also assumes that you have already prepared your data 
and metadata to comply with Darwin Core standards.  If you have not done 
this, please see our Darwin Core data package, `corella <corella.ala.org.au/Python>`_ 
and `delma <delma.ala.org.au/Python>`_.

Initialising a Darwin Core Archive
--------------------------------------

For a Darwin Core Archive containing only a list of occurrences, the 
process is relatively straightforward.  For this example, we will assume 
that all the data has been formatted to comply with Dariwn Core Archive 
standards, and the variable name is ``df``.  We will also assume that your 
metadata has been filled in, correctly rendered and is named ``eml.xml``.

First, we will create the Darwin Core Archive object, and specify our 
occurrences and metadata.  This will automatically assume you want to make 
a directory in the folder you are working in.  If you want to specify a different 
folder, you can set the variable ``working_dir=<NAME>``.

.. prompt:: Python

    >>> import galaxias
    >>> my_dwca = galaxias.dwca(occurrences=df,
    ...                         eml_xml='eml.xml')

This will create a ``dwca`` object with all of your information in one place.  
Now, we will create the ``meta.xml`` file.  

Metadata files in a Darwin Core Archive
-------------------------------------------

Darwin Core Archives require two metadata files: one to describe the dataset 
itself (i.e. what license is attached to it, who collected the data, etc.), 
and one to describe the Darwin Core Archive itself.  The former is the ``eml.xml`` 
file you provided above, while the other is the one we will create right now.  
If you use the function

.. prompt:: Python

    >>> my_dwca.make_meta_xml()

it will create a file called ``meta.xml`` in your working directory.  This contains 
a list of the files in the archive, as well as a list of what is in the data files (
in this case, occurrences).  

Creating a Darwin Core Archive
-------------------------------------------

If you have not gotten any errors thus far, and are happy with your filenames being the 
default in ``galaxias``, you can now run

    >>> my_dwca.create_dwca()

This will produce a Darwin Core Archive titled ``dwca.zip``, which contains the files ``occurrences.csv``, 
``eml.xml`` and ``meta.xml``.  