from main import ElementNode, TextNode, parse


def test_nested_structure_builds_tree():
    tokens = [
        {"type": "StartTag", "name": "div"},
        {"type": "Text", "data": "Hi "},
        {"type": "StartTag", "name": "b"},
        {"type": "Text", "data": "there"},
        {"type": "EndTag", "name": "b"},
        {"type": "EndTag", "name": "div"},
    ]

    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert len(root.children) == 1  # Root has one child: the div

    div = root.children[0]
    assert div.name == "div"
    assert len(div.children) == 2

    text_child = div.children[0]
    bold_child = div.children[1]

    assert isinstance(text_child, TextNode)
    assert text_child.data == "Hi "

    assert isinstance(bold_child, ElementNode)
    assert bold_child.name == "b"
    assert len(bold_child.children) == 1
    assert isinstance(bold_child.children[0], TextNode)
    assert bold_child.children[0].data == "there"


def test_multiple_siblings_under_root():
    tokens = [
        {"type": "StartTag", "name": "p"},
        {"type": "Text", "data": "first"},
        {"type": "EndTag", "name": "p"},
        {"type": "StartTag", "name": "p"},
        {"type": "Text", "data": "second"},
        {"type": "EndTag", "name": "p"},
    ]

    # parse should attach siblings at the top level under an implicit root
    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert len(root.children) == 2
    assert all(isinstance(child, ElementNode) for child in root.children)
    assert [child.name for child in root.children] == ["p", "p"]
    assert [child.children[0].data for child in root.children] == ["first", "second"]


def test_text_only_input_creates_text_child_under_root():
    tokens = [{"type": "Text", "data": "just text"}]

    root = parse(tokens)

    assert isinstance(root, ElementNode)
    assert len(root.children) == 1
    assert isinstance(root.children[0], TextNode)
    assert root.children[0].data == "just text"


def test_attributes_are_preserved_on_element_nodes():
    tokens = [
        {"type": "StartTag", "name": "div", "attrs": {"id": "main"}},
        {"type": "Text", "data": "body"},
        {"type": "EndTag", "name": "div"},
    ]

    root = parse(tokens)

    div = root.children[0]
    assert isinstance(div, ElementNode)
    assert div.attrs == {"id": "main"}
