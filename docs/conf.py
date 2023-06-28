# -- Project information -----------------------------------------------------

project = 'FelooPy'
copyright = '2023, Keivan Tafakkori'
author = 'Keivan Tafakkori'

# -- General configuration ---------------------------------------------------

extensions = ['myst_parser', 'sphinx_copybutton']

source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'

html_logo = "_static/logo.png"

html_css_files = [
    '_static/custom.css',
]


