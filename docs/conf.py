# -- Project information -----------------------------------------------------

project = 'FelooPy'
copyright = '2023, Keivan Tafakkori'
author = 'Keivan Tafakkori'

# -- General configuration ---------------------------------------------------

extensions = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'base_url': '/',
    'color_primary': 'indigo',
    'color_accent': 'grey',
    'repo_url': 'https://github.com/ktafakkori/feloopy/',
    'repo_name': 'feloopy',
    "logo": {
        "text": "FelooPy's Documentation",
        "image_dark": "_static/logo.svg",
        "alt_text": "FelooPy's Documentation",
    }
}

html_logo = "_static/logo3.png"

html_css_files = ["custom.css"]
