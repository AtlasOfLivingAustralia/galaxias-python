# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import galaxias

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Galaxias'
copyright = '2024, Amanda Buyan, Atlas of Living Australia'
author = 'Amanda Buyan, Atlas of Living Australia'

# add path for galaxias
sys.path.insert(0,"../../galaxias/src/galaxias/")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'myst_parser',
	'sphinx-prompt',
	'sphinxcontrib.programoutput',
	'sphinx_design',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton'
]

autosectionlabel_prefix_document = True
napoleon_use_param = True

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []

version = str(galaxias.__version__)
release = version
source_path = os.path.dirname(os.path.abspath(__file__))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
	"navbar_align": "content",
	"github_url": "https://github.com/AtlasOfLivingAustralia/galaxias-python",
	"secondary_sidebar_items": ["page-toc"],
    "logo": {
		"image_light": "_static/logo/cake_logo.png", # didn't have dir before
        "image_dark": "_static/logo/cake_logo.png", 
	},
}

# was image_light
html_sidebars = {
	"index": [],
	"search": [],
    "**": ["sidebar-nav-bs"]
}

html_static_path = ['_static']

# html_logo = "_static/logo/logo.png"

html_logo = "_static/logo/cake_logo.png"

# html_favicon = '_static/logo/favicon.ico'

html_css_files = ['css/extra.css']

html_style = 'css/extra.css'