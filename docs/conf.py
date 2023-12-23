# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FelooPy'
copyright = '2023, Keivan Tafakkori'
author = 'Keivan Tafakkori'
release = '0.2.8'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add these lines to make your project discoverable
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx_book_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    'm2r',
]

# Exclude patterns including '_build' and 'Thumbs.db', and add 'extras' to exclude_patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/extras']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    'repository_url': 'https://github.com/ktafakkori/feloopy',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
}

html_static_path = ['_static']

html_logo = "miscellaneous/logo/logo1.png"

# For Mermaid
mermaid_output_format = 'png'

# For terminal code blocks
pygments_style = 'sphinx'