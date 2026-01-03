"""Tests for multi-line HTML parsing with various whitespace characters."""
from problem4 import tokenize, parse


def test_multiline_html_with_indentation():
    """Real-world HTML files have newlines and indentation."""
    html = """<div class="container">
  <h1>Title</h1>
  <p>Content</p>
</div>"""

    tokens = tokenize(html)
    root = parse(tokens)

    # Should parse without errors
    assert len(root.children) == 1
    assert root.children[0].name == "div"


def test_tabs_between_tag_and_attributes():
    """Attributes can be separated by tabs, not just spaces."""
    html = '<img\tsrc="logo.png"\talt="Logo" />'

    tokens = tokenize(html)

    assert len(tokens) == 1
    assert tokens[0]["type"] == "SelfClosingTag"
    assert tokens[0]["name"] == "img"
    assert tokens[0]["attrs"] == {"src": "logo.png", "alt": "Logo"}


def test_newlines_in_tag_attributes():
    """Attributes can span multiple lines."""
    html = '''<img
    src="logo.png"
    alt="Logo"
/>'''

    tokens = tokenize(html)

    assert len(tokens) == 1
    assert tokens[0]["name"] == "img"
    assert tokens[0]["attrs"] == {"src": "logo.png", "alt": "Logo"}


def test_mixed_whitespace_in_attributes():
    """Mix of spaces, tabs, and newlines."""
    html = '<div  \t\n  class="test"  \t  id="main">'

    tokens = tokenize(html)

    assert tokens[0]["attrs"] == {"class": "test", "id": "main"}


def test_whitespace_only_text_nodes():
    """Whitespace between tags becomes text nodes."""
    html = "<div>\n  <span>text</span>\n</div>"

    tokens = tokenize(html)

    # Should have: StartTag(div), Text(\n  ), StartTag(span), Text(text),
    #              EndTag(span), Text(\n), EndTag(div)
    assert len(tokens) == 7
    assert tokens[1]["type"] == "Text"
    assert tokens[1]["data"] == "\n  "
    assert tokens[5]["type"] == "Text"
    assert tokens[5]["data"] == "\n"
