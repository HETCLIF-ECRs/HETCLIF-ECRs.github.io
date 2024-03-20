# Configuration file for the Sphinx documentation builder.

import pydata_sphinx_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HETCLIF ECRs'
copyright = '2024, HETCLIF ECRs'
author = 'Ankit Bhandekar'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_sidebars = {
  "**": []
}

html_theme_options = {
    "logo": {
        "text": "HETCLIF ECRs",
    },
    # "external_links": [
    #     {"name": "GitHub", "url": "https://github.com/HETCLIF-ECRs/hetclif-ecrs.github.io"}
    # ],
    "navigation_with_keys": False,
}

html_show_sourcelink = False

