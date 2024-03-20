# Configuration file for the Sphinx documentation builder.

import pydata_sphinx_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HETCLIF ECRs'
copyright = '2024, HETCLIF ECRs'
author = 'Ankit Bhandekar'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.insert(0, os.path.abspath("."))

extensions = [
    "sphinx_favicon",
]

source_dir = 'source'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_sidebars = {
  "**": []
}

html_title = "HETCLIF ECRs"
html_logo = '_static/logo.png'
html_baseurl = 'https://HETCLIF-ECRs.github.io/'
html_show_sourcelink = False
html_theme_options = {
    "logo": {
        "text": "HETCLIF ECRs",
        "image_dark": "_static/logo.png",  # assuming your logo file is named logo.png and located in the _static directory
        "alt_text": "HETCLIF ECRs",
    },
    "footer_end": ["combined_footer.html"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
        "navbar_persistent": [],  # Make sure the search button is not included here
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/orgs/HETCLIF-ECRs/discussions",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Slack",
            "url": "https://hetclif.slack.com/archives/C068H4XAQS3",
            "icon": "fa-brands fa-slack",
        },
        # Add any other icon links here
    ],
}

# -- Option for favicons -------------------------------------------------------
favicons = [
    "favicon.png"
]

def setup(app):
    app.add_css_file('basic.css')
    # Make sure to include the Font Awesome CSS for icons if it's not already included
    app.add_css_file('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css')




