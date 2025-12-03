import pytest

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
