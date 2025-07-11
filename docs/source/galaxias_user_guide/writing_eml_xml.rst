:orphan:

Creating your metadata
------------------------------

Using ``galaxias`` to turn markdown into EML will require only two steps, with two optional 
steps for troubleshooting.

Create your initial markdown file
=====================================

First, you will need to have a markdown metadata file.  ``galaxias`` comes with a default, recommended 
one for the Atlas of Living Australia.  To generate this, simply type

.. prompt:: python

   >>> import galaxias
   >>> my_dwca = galaxias.dwca()

What this will do is create a ``dwca`` object, with a file titled ``metadata.md``, in your 
current directory.  If you want to change either the name of the metadata file, or where it 
is placed, you can edit the following two variables when you make the ``dwca`` object:

- ``metadata_md``: this will change the name of the markdown file.
- ``working_dir``: this will change where the markdown file is written.

.. note::

   If you have a template xml that you would like to use instead, ``galaxias`` will accept that too.  
   Just provide a link/file when you create the ``dwca`` object, like so:

   .. prompt:: python

      >>> my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368")

Editing your markdown file
================================

Now comes the more involved part: editing your markdown.  We have a boilerplate metadata markdown statement, 
which is the minimum amount of metadata the ALA requires.  When editing, remember two things:

1. Don't add anything to the words with hashes (`#`) in front of them.  These are headings, and will therefore be formatted in the XML file
2. Leave a space between your added text and the next word with a hash in front of it.

.. note:: Checking your markdown file

   ``galaxias`` has a function where you can check if your markdown is formatted correctly, and all 
   metadata values are consistent.  To do this, run 

   .. prompt:: python

        >>> my_dwca.display_metadata_as_dataframe()

   .. program-output:: python galaxias_user_guide/metadata_run.py

Writing your metadata file
===============================

After you have successfully edited your markdown file, it is time to write your metadata xml file.  
To do so, run

.. prompt:: python

   >>> galaxias.write_eml()

These are all the possible arguments for ``write_eml()``.  What is shown is the default values 
for these arguments, so if you decide to go with all the defaults, you do not have to include these 
arguments.

Validating your xml file
=================================

If you are concerned about the formatting of your ``eml.xml`` file, we have an in-built function 
that will validate its formatting again a GBIF template.  To run this check, type

.. prompt:: python

   >>> galaxias.check_metadata()

If it is a valid ``eml.xml``, you will not get an error message.  Various error messages will 
appear if something is not formatted correctly.