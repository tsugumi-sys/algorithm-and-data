from main import tokenize


def test_start_tag_with_multiple_attributes():
    input_html = '<div id="main" class="c1 c2">Hello</div>'
    expected = [
        {"type": "StartTag", "name": "div", "attrs": {"id": "main", "class": "c1 c2"}},
        {"type": "Text", "data": "Hello"},
        {"type": "EndTag", "name": "div"},
    ]
    assert tokenize(input_html) == expected


def test_self_closing_like_img_is_treated_as_start_tag_with_attrs():
    input_html = '<img src="a.png" alt="logo">'
    expected = [
        {
            "type": "StartTag",
            "name": "img",
            "attrs": {"src": "a.png", "alt": "logo"},
        }
    ]
    assert tokenize(input_html) == expected


def test_text_nodes_preserve_spaces_outside_attributes():
    input_html = '<a href="https://example.com">Link</a>'
    expected = [
        {"type": "StartTag", "name": "a", "attrs": {"href": "https://example.com"}},
        {"type": "Text", "data": "Link"},
        {"type": "EndTag", "name": "a"},
    ]
    assert tokenize(input_html) == expected


def test_start_tag_without_attributes():
    input_html = "<div>Hello</div>"
    expected = [
        {"type": "StartTag", "name": "div", "attrs": {}},
        {"type": "Text", "data": "Hello"},
        {"type": "EndTag", "name": "div"},
    ]
    assert tokenize(input_html) == expected


def test_attribute_value_contains_spaces():
    input_html = '<p title="hello world example">Hi</p>'
    expected = [
        {"type": "StartTag", "name": "p", "attrs": {"title": "hello world example"}},
        {"type": "Text", "data": "Hi"},
        {"type": "EndTag", "name": "p"},
    ]
    assert tokenize(input_html) == expected


def test_multiple_attributes_are_all_parsed():
    input_html = '<span data-id="42" aria-label="hello">X</span>'
    expected = [
        {
            "type": "StartTag",
            "name": "span",
            "attrs": {"data-id": "42", "aria-label": "hello"},
        },
        {"type": "Text", "data": "X"},
        {"type": "EndTag", "name": "span"},
    ]
    assert tokenize(input_html) == expected
