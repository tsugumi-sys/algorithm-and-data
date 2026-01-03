import pytest
from html_parser import HTMLParser, Node


def test_empty_input_returns_document_node():
    """Document node exists even for empty input"""
    parser = HTMLParser()
    root = parser.parse("")

    assert isinstance(root, Node)
    assert root.type == "document"
    assert root.tag is None
    assert root.children == []


def test_single_element_with_text_node():
    """Parse a single element that wraps one text node"""
    parser = HTMLParser()
    root = parser.parse("<p>Hello</p>")

    assert len(root.children) == 1
    paragraph = root.children[0]
    assert paragraph.type == "element"
    assert paragraph.tag == "p"
    assert paragraph.attributes == {}
    assert len(paragraph.children) == 1
    text = paragraph.children[0]
    assert text.type == "text"
    assert text.text == "Hello"
    assert text.children == []


def test_nested_elements_and_siblings_are_in_order():
    """Nested children and sibling order is preserved"""
    parser = HTMLParser()
    root = parser.parse("<div><span>first</span><span>second</span></div>")

    div = root.children[0]
    assert div.tag == "div"
    assert [child.tag for child in div.children if child.type == "element"] == [
        "span",
        "span",
    ]
    first, second = div.children
    assert first.children[0].text == "first"
    assert second.children[0].text == "second"


def test_attributes_are_parsed_with_insertion_order():
    """Attributes use double quotes and preserve order"""
    parser = HTMLParser()
    root = parser.parse('<div class="note" data-id="42"></div>')

    div = root.children[0]
    assert div.attributes == {"class": "note", "data-id": "42"}
    assert list(div.attributes.keys()) == ["class", "data-id"]


def test_self_closing_tags_become_leaf_nodes():
    """Self-closing tags produce element nodes without children"""
    parser = HTMLParser()
    root = parser.parse("<p>Hello<br/>World</p>")

    paragraph = root.children[0]
    assert paragraph.tag == "p"
    assert [child.type for child in paragraph.children] == [
        "text",
        "element",
        "text",
    ]
    text_before, br, text_after = paragraph.children
    assert br.tag == "br"
    assert br.children == []
    assert text_before.text == "Hello"
    assert text_after.text == "World"


def test_preserves_whitespace_in_text_nodes():
    """Whitespace inside text nodes is not normalized"""
    parser = HTMLParser()
    html = "<p>  Hello \n  World  </p>"
    root = parser.parse(html)

    paragraph = root.children[0]
    assert paragraph.children[0].text == "  Hello \n  World  "


def test_multiple_top_level_elements_allowed():
    """Document node can contain multiple root children"""
    parser = HTMLParser()
    root = parser.parse("<p>One</p><p>Two</p>")

    assert len(root.children) == 2
    assert [child.tag for child in root.children] == ["p", "p"]
    assert [child.children[0].text for child in root.children] == ["One", "Two"]


def test_mismatched_closing_tag_raises():
    """Mismatched tags produce a ValueError"""
    parser = HTMLParser()
    with pytest.raises(ValueError):
        parser.parse("<div><span></div>")


def test_unexpected_closing_tag_raises():
    """A stray closing tag fails parsing"""
    parser = HTMLParser()
    with pytest.raises(ValueError):
        parser.parse("</p>")


def test_unclosed_tag_at_end_of_input_raises():
    """Open tags must be closed before the input ends"""
    parser = HTMLParser()
    with pytest.raises(ValueError):
        parser.parse("<div>")
