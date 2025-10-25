# pyproject.toml example for Black
"""
[tool.black]
line-length = 88           # default line length
skip-string-normalization = false  # keeps string quotes as you write them
"""

# or using a Python dictionary for custom formatting logic
FORMAT_CONFIG = {
    "use_tabs": False,         # Use spaces instead of tabs
    "indent_size": 2,          # Tab width equivalent
    "quote_style": "single",   # Prefer single quotes
    "bracket_spacing": True,   # Spacing inside brackets
}
