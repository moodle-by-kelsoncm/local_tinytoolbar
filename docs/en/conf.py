import moodle_docs_theme

project = "moodle-local_tinytoolbar"
copyright = "2024, Kelson da Costa Medeiros"
author = "Kelson da Costa Medeiros"
release = "1.0.0"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "project_name": "moodle-local_tinytoolbar",
    "tagline": "Visual toolbar customizer for TinyMCE in Moodle",
    "github_url": "https://github.com/moodle-by-kelsoncm/local_tinytoolbar",
    "github_repo": "moodle-by-kelsoncm/local_tinytoolbar",
    "github_version": "main",
    "doc_path": "docs/en/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "enable_language_selector": True,
    "navigation_links": "Home|index, Installation|installation, Configuration|configuration, Usage|usage",
}

html_static_path = []
