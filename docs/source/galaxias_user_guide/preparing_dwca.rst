:orphan:

Preparing the DwCA itself 
==========================

At the end of the above process, we should have a folder named data-publish that contains at least two files:

- One or more ``.csv`` files containing data (e.g. ``occurrences.csv``, ``events.csv``, ``multimedia.csv``)
- An ``eml.xml`` file containing your metadata

We can now run ``build_archive()`` to build our Darwin Core Archive!

.. prompt:: Python

    >>> galaxias.build_archive()

Running ``build_archive()`` first checks whether we have a ‘schema’ document (``meta.xml``) in our ``data-publish`` 
folder. This is a machine-readable xml document that describes the content of the archive’s data files and their 
structure. The schema document is a required file in a Darwin Core Archive. If it is missing, ``build_archive()`` 
will build one. We can also build a schema document ourselves using ``use_schema()``.

At the end of this process, you should have a Darwin Core Archive zip file (``dwca.zip``) in your parent directory. 
You should also have a ``data-publish`` folder in your working directory containing standardised data files 
(e.g. ``occurrences.csv``), a metadata statement in EML format (``eml.xml``), and a schema document (``meta.xml``).