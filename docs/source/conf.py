# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[0]))

# Point this to the directory containing your Python source files (ca sa apara si in api in tabel, poate sa vada fisierele si atunci extrage din ele)
sys.path.insert(0, os.path.abspath('../src')) 

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'lumache'
copyright = '2026, Mihaiela'
author = 'Mihaiela'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

# By default, the .. autosummary:: directive only creates a clean,
#  compact summary table of your code elements on a single page. 
# If a user clicks on a function name in that table, Sphinx looks for a separate page (a "stub" file)
#  detailing that specific function.Without autosummary_generate = True, those links will lead to broken "404 Not Found" 
# errors because Sphinx does not create those sub-pages on its own
#!!!!!!!!!!!!!!!!! cred ca asta te ajuta sa ai ambele pagini fara sa dispara
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_static_path = ['_static']