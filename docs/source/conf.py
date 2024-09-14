"""Configuration file for the Sphinx documentation builder."""

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "bluesky_session"
copyright = "2023-2024, APS BCDA"
author = "APS BCDA"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = """
    IPython.sphinxext.ipython_console_highlighting
    IPython.sphinxext.ipython_directive
    sphinx.ext.autodoc
    sphinx.ext.autosummary
    sphinx.ext.coverage
    sphinx.ext.githubpages
    sphinx.ext.inheritance_diagram
    sphinx.ext.mathjax
    sphinx.ext.todo
    sphinx.ext.viewcode
    nbsphinx
    myst_parser
""".split()
myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
source_suffix = ".rst .md".split()
exclude_patterns = ["**.ipynb_checkpoints"]

today_fmt = "%Y-%m-%d %H:%M"

# Ignore errors in notebooks while documenting them
nbsphinx_allow_errors = True

# autodoc
autodoc_default_options = {
    'members': True,
    'private-members': True,
    'member-order': True,
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
    "show-inheritance": True,
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_title = project

autodoc_mock_imports = """
    bluesky
    databroker
    epics
    intake
    matplotlib
    numpy
    ophyd
    ophydregistry
    pandas
""".split()
