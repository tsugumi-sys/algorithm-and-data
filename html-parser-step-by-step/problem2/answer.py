import re

TAG_PATTERN = re.compile(r"[a-zA-Z][a-zA-Z0-9]*")
ATTR_NAME_PATTERN = re.compile(r"[a-zA-Z][a-zA-Z0-9._:-]*")

TAG_START = "<"
TAG_END = ">"


def tokenize(html: str) -> list[dict[str, str | dict]]:
    pos = 0  # pointer
    tokens = []

    while pos < len(html):
        if html[pos] == TAG_START:
            # consume tag
            tag_type, tag_name, pos = consume_tag(html, pos)
            tag_token = {"type": tag_type, "name": tag_name}
            if tag_type == "StartTag":
                tag_token["attrs"] = {}
            if html[pos] != TAG_END:
                attrs, pos = consume_attributes(html, pos)
                tag_token["attrs"] = attrs
            pos = consume(html, pos, TAG_END)
            tokens.append(tag_token)
        else:
            text, pos = consume_text(html, pos)
            tokens.append({"type": "Text", "data": text})
    return tokens


def consume_text(html: str, pos: int) -> tuple[str, int]:
    start = pos
    while pos < len(html) and html[pos] != TAG_START:
        pos += 1
    return html[start:pos], pos


def consume_tag(
    html: str, pos: int
) -> tuple[str, str, int]:  # tag type, tag name, position.
    if html[pos] != TAG_START:
        raise ValueError("Unexpected value for tag start")
    pos += 1
    if pos > len(html):
        raise ValueError("Invalid html")
    if html[pos] == "/":
        tag_type = "EndTag"
        pos += 1
    else:
        tag_type = "StartTag"
    start = pos
    while pos < len(html) and html[pos] != TAG_END and not html[pos].isspace():
        pos += 1
    tag_name = html[start:pos]
    if not TAG_PATTERN.fullmatch(tag_name):
        raise ValueError("Invalid tag name")
    return tag_type, tag_name, pos


def consume_attributes(
    html: str, pos: int
) -> tuple[dict[str, str], int]:  # attributes, position
    if html[pos].isspace():
        pos = consume_white_spaces(html, pos)
    attrs = {}
    while pos < len(html) and html[pos] != TAG_END:
        attr_name, pos = consume_attributes_name(html, pos)
        if not ATTR_NAME_PATTERN.fullmatch(attr_name):
            raise ValueError("Invalid attribute name")
        pos = consume(html, pos, "=")
        pos = consume(html, pos, '"')  # value start
        attr_value, pos = consume_attributes_value(html, pos)
        pos = consume(html, pos, '"')  # value end
        attrs[attr_name] = attr_value
        pos = consume_white_spaces(html, pos)
    return attrs, pos


def consume_attributes_name(
    html: str, pos: int
) -> tuple[str, int]:  # attribute name & position
    start = pos
    while pos < len(html) and html[pos] != "=":
        pos += 1
    attr_name = html[start:pos]
    return attr_name, pos


def consume_attributes_value(
    html: str, pos: int
) -> tuple[str, int]:  # attribute name & position
    start = pos
    while pos < len(html) and html[pos] != '"':
        pos += 1
    return html[start:pos], pos


def consume(html: str, pos: int, pattern: str):
    if not html[pos:].startswith(pattern):
        raise ValueError("the pattern is not found")
    pos += len(pattern)
    return pos


def consume_white_spaces(html: str, pos: int) -> int:
    while pos < len(html) and html[pos].isspace():
        pos += 1
    return pos
