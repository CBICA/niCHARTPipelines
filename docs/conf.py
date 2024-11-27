# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../"))

project = "NiChart_DLMUSE"
copyright = "2024, Ashish Singh, Guray Erus, George Aidinis"
author = "Ashish Singh, Guray Erus, George Aidinis"
release = "2024"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'nipype.sphinxext.apidoc',
    'nipype.sphinxext.plot_workflow',
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'sphinx_markdown_tables',
    'sphinxarg.ext',
    'sphinxcontrib.apidoc',
    'sphinxcontrib.bibtex',
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

github_username = "CBICA"
github_repository = "github.com/CBICA/NiChart_DLMUSE"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
