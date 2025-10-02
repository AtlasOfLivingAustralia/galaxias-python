.. _Installation:

Installation
==============

*Note: if you prefer to install prerequisites first, see below section*

To install ``galaxias-python``, type the following into the terminal:

.. prompt:: bash

    pip install galaxias-python

For those who want the latest version (or the development version) via Github, 
type the following:

.. prompt:: bash

    git clone https://github.com/AtlasOfLivingAustralia/galaxias-python.git
    pip install .

Prerequisites
------------------

ou will need the following packages to be able to run ``galah``:

- `pandas <https://pandas.pydata.org/>`_
- `beautifulsoup4 <https://beautiful-soup-4.readthedocs.io/en/latest/>`_
- `configparser <https://pypi.org/project/configparser/>`_
- `pytest <https://pypi.org/project/pytest/>`_
- `requests <https://requests.readthedocs.io/en/latest/>`_
- `shutils <https://pypi.org/project/shutils/>`_
- `tabulate <https://pypi.org/project/tabulate/>`_
- `corella-python <https://pypi.org/project/corella-python/>`_
- `delma-python <https://pypi.org/project/delma-python/>`_

To install all of these at once, run

.. prompt:: 

    pip install pandas beautifulsoup4 configparser pytest requests shutils tabulate corella-python delma-python

WARNING: If you're installing all of the packages in one go, make sure you check that the installation ran successfully.  If one package doesnt work, the rest following wont install...