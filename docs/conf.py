# -- Project information -----------------------------------------------------

project = 'FelooPy'
copyright = '2023, Keivan Tafakkori'
author = 'Keivan Tafakkori'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    "autoapi.extension",
    "_extension.gallery_directive",
    # For extension examples and demos
    "ablog",
    "jupyter_sphinx",
    "matplotlib.sphinxext.plot_directive",
    "myst_nb",
    "sphinxcontrib.youtube",
    # "nbsphinx",  # Uncomment and comment-out MyST-NB for local testing purposes.
    "numpydoc",
    "sphinx_togglebutton",
    "jupyterlite_sphinx",
    "sphinx_favicon",
]

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
