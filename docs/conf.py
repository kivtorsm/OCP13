# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django


sys.path.insert(0, os.path.abspath('..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OCP13'
copyright = '2023, vsm'
author = 'vsm'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    "sphinxcontrib_django",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Autodoc --------------------------------------------------------

autodoc_mock_imports = ["lettings.models", "views"]
autosummary_imported_members = False
numpydoc_show_class_members = False
autosummary_generate_overwrite = False


# Configure the path to the Django settings module
django_settings = "oc_lettings_site.settings"

# Include the database table names of Django models
django_show_db_tables = True                # Boolean, default: False
# Add abstract database tables names (only takes effect if django_show_db_tables is True)
django_show_db_tables_abstract = True       # Boolean, default: False