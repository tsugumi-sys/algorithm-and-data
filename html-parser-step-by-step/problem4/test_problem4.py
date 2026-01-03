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
    assert len(root.children) == 1  # Root has one child: the div

    div = root.children[0]
    assert div.name == "div"
    assert [type(child) for child in div.children] == [TextNode, ElementNode, TextNode]
    assert div.children[0].data == "Hello"
    assert div.children[1].name == "br"
    assert div.children[1].children == []
    assert div.children[2].data == "World"


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


def test_multiple_self_closing_siblings():
    tokens = [
        {"type": "SelfClosingTag", "name": "img", "attrs": {"src": "a.png"}},
        {"type": "SelfClosingTag", "name": "img", "attrs": {"src": "b.png"}},
    ]

    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert len(root.children) == 2
    assert [child.name for child in root.children] == ["img", "img"]
    assert [child.attrs for child in root.children] == [
        {"src": "a.png"},
        {"src": "b.png"},
    ]


def test_tokenize_self_closing_at_start_of_input():
    input_html = "<br/>line"
    expected = [
        {"type": "SelfClosingTag", "name": "br"},
        {"type": "Text", "data": "line"},
    ]
    assert tokenize(input_html) == expected
