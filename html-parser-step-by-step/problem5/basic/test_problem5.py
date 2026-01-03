
from problem5 import ElementNode, TextNode, parse, tokenize


def test_parser_closes_missing_end_tags_gracefully():
    tokens = tokenize("<div><b>bold</div>")
    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert root.name == "div"
    assert len(root.children) == 1

    bold = root.children[0]
    assert isinstance(bold, ElementNode)
    assert bold.name == "b"
    assert len(bold.children) == 1
    assert isinstance(bold.children[0], TextNode)
    assert bold.children[0].data == "bold"


def test_unexpected_end_tag_pops_until_match():
    tokens = [
        {"type": "StartTag", "name": "div"},
        {"type": "StartTag", "name": "span"},
        {"type": "Text", "data": "hi"},
        {"type": "EndTag", "name": "div"},
    ]

    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert root.name == "div"
    assert len(root.children) == 1
    span = root.children[0]
    assert isinstance(span, ElementNode)
    assert span.name == "span"
    assert len(span.children) == 1
    assert isinstance(span.children[0], TextNode)
    assert span.children[0].data == "hi"


def test_nested_unclosed_tags_are_closed_at_end():
    tokens = tokenize("<div><b><i>deep</div>")
    root = parse(tokens)

    div = root.children[0]
    bold = div.children[0]
    italic = bold.children[0]

    assert isinstance(div, ElementNode)
    assert isinstance(bold, ElementNode)
    assert isinstance(italic, ElementNode)
    assert italic.children[0].data == "deep"


def test_trailing_unclosed_top_level_tag():
    tokens = tokenize("<section>content")
    root = parse(tokens)

    assert len(root.children) == 1
    section = root.children[0]
    assert isinstance(section, ElementNode)
    assert [child.data for child in section.children] == ["content"]
