import pytest

from main import tokenize


def test_empty():
    input_html = ""
    expected = []
    assert tokenize(input_html) == expected


def test_simple_tag_then_text_then_end_tag():
    input_html = "<div>Hello</div>"
    expected = [("TAG", "div"), ("TEXT", "Hello"), ("TAG", "/div")]
    assert tokenize(input_html) == expected


def test_text_br_text():
    input_html = "Hi<br>there"
    expected = [("TEXT", "Hi"), ("TAG", "br"), ("TEXT", "there")]
    assert tokenize(input_html) == expected


def test_nested_tags_remain_flat():
    input_html = "<p>A <b>bold</b> move</p>"
    expected = [
        ("TAG", "p"),
        ("TEXT", "A "),
        ("TAG", "b"),
        ("TEXT", "bold"),
        ("TAG", "/b"),
        ("TEXT", " move"),
        ("TAG", "/p"),
    ]
    assert tokenize(input_html) == expected


def test_text_only_is_single_text_token():
    input_html = "plain text"
    expected = [("TEXT", "plain text")]
    assert tokenize(input_html) == expected


def test_text_allows_punctuation_and_digits():
    input_html = "Hello! 123, world?"
    expected = [("TEXT", "Hello! 123, world?")]
    assert tokenize(input_html) == expected


def test_tag_name_can_include_digits_not_at_start():
    input_html = "<h1>Title</h1>"
    expected = [("TAG", "h1"), ("TEXT", "Title"), ("TAG", "/h1")]
    assert tokenize(input_html) == expected


def test_error_on_unterminated_tag():
    with pytest.raises(ValueError):
        tokenize("<div")


def test_error_on_tag_starting_with_digit():
    with pytest.raises(ValueError):
        tokenize("<1div>")
