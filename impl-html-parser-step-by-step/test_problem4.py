import pytest

from problem4 import ElementNode, TextNode, parse, tokenize


def test_tokenize_marks_self_closing_tag():
    input_html = "<div>Hello<br/>World</div>"
    expected = [
        {"type": "StartTag", "name": "div"},
        {"type": "Text", "data": "Hello"},
        {"type": "SelfClosingTag", "name": "br"},
        {"type": "Text", "data": "World"},
        {"type": "EndTag", "name": "div"},
    ]
    assert tokenize(input_html) == expected


def test_parse_handles_self_closing_without_stack_push():
    tokens = [
        {"type": "StartTag", "name": "div"},
        {"type": "Text", "data": "Hello"},
        {"type": "SelfClosingTag", "name": "br"},
        {"type": "Text", "data": "World"},
        {"type": "EndTag", "name": "div"},
    ]

    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert root.name == "div"
    assert [type(child) for child in root.children] == [TextNode, ElementNode, TextNode]
    assert root.children[0].data == "Hello"
    assert root.children[1].name == "br"
    assert root.children[1].children == []
    assert root.children[2].data == "World"


def test_self_closing_tag_can_carry_attributes():
    input_html = '<img src="logo.png" alt="logo" />'
    expected = [
        {
            "type": "SelfClosingTag",
            "name": "img",
            "attrs": {"src": "logo.png", "alt": "logo"},
        }
    ]
    assert tokenize(input_html) == expected
