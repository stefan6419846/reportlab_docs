# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from importlib.metadata import metadata as _metadata


metadata = _metadata("reportlab")

project = "reportlab"
copyright = metadata["License"]
author = metadata["Author"]
version = release = metadata["Version"]

# General configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx", "myst_parser"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

nitpicky = True


# Options for HTML output
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

master_doc = "index"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


# Options for cross-referencing.

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
