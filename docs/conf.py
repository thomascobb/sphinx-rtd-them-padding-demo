import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..")))

extensions = ["sphinx.ext.autodoc"]
html_theme = "sphinx_rtd_theme"
