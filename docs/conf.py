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
    "icon_links": [
        {
            "name": "PyData",
            "url": "https://github.com/ktafakkori/feloopy/",
            "icon": "_static/logo3.png",
            "type": "local",
            "attributes": {"target": "_blank"},
        },
    ]

}

html_logo = "_static/logo3.png"

html_css_files = ["custom.css"]
