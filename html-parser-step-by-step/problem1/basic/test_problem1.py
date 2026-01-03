from problem1 import tokenize


def test_start_and_end_tags_are_distinct_tokens():
    input_html = "<div>Hello</div>"
    expected = [
        {"type": "StartTag", "name": "div"},
        {"type": "Text", "data": "Hello"},
        {"type": "EndTag", "name": "div"},
    ]
    assert tokenize(input_html) == expected


def test_detects_end_tag_via_leading_slash():
    input_html = "A<br>B"
    expected = [
        {"type": "Text", "data": "A"},
        {"type": "StartTag", "name": "br"},
        {"type": "Text", "data": "B"},
    ]
    assert tokenize(input_html) == expected


def test_multiple_text_segments_are_preserved():
    input_html = "<p>A <b>bold</b> move</p>"
    expected = [
        {"type": "StartTag", "name": "p"},
        {"type": "Text", "data": "A "},
        {"type": "StartTag", "name": "b"},
        {"type": "Text", "data": "bold"},
        {"type": "EndTag", "name": "b"},
        {"type": "Text", "data": " move"},
        {"type": "EndTag", "name": "p"},
    ]
    assert tokenize(input_html) == expected


def test_text_before_and_after_tags():
    input_html = "before<div>inside</div>after"
    expected = [
        {"type": "Text", "data": "before"},
        {"type": "StartTag", "name": "div"},
        {"type": "Text", "data": "inside"},
        {"type": "EndTag", "name": "div"},
        {"type": "Text", "data": "after"},
    ]
    assert tokenize(input_html) == expected


def test_consecutive_tags_without_text():
    input_html = "<br><hr>"
    expected = [
        {"type": "StartTag", "name": "br"},
        {"type": "StartTag", "name": "hr"},
    ]
    assert tokenize(input_html) == expected


def test_empty_input_returns_empty_list():
    assert tokenize("") == []
