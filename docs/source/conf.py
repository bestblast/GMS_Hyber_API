# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'JSON V2Protocol'
copyright = '2022, GMS'
author = 'GMS'

release = '2.2'
version = '2.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

import os
import sys

sys.path.insert(0, os.path.abspath('_ext'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions # coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['jsonlexer']
