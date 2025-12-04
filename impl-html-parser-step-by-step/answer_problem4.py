from typing import Self
from dataclasses import dataclass, field
import re

TAG_PATTERN = re.compile(r"[a-zA-Z][a-zA-Z0-9]*")
ATTR_PATTERN = re.compile(r"[a-zA-Z][a-zA-Z0-9_-]*")

type Attributes = dict[str, str]
type Tokens = list[dict[str, str | dict[str, str]]]


@dataclass
class ElementNode:
    name: str
    attrs: Attributes = field(default_factory=dict)
    children: list[Self] = field(default_factory=list)


@dataclass
class TextNode:
    data: str


TAG_START = "<"
TAG_END = ">"
START_TAG_TYPE = "StartTag"
END_TAG_TYPE = "EndTag"
SELF_CLOSING_TAG_TYPE = "SelfClosingTag"
TEXT_TAG_TYPE = "Text"


def tokenize(html: str) -> Tokens:
    pos = 0
    tokens = []
    while pos < len(html):
        if html[pos] == TAG_START:
            # consume TAG_START
            pos = consume(html, pos, TAG_START)
            # consume tag name
            tag_name, tag_type, attrs, pos = consume_tag_name(html, pos)
            if attrs:
                tokens.append({"type": tag_type, "name": tag_name, "attrs": attrs})
            else:
                tokens.append({"type": tag_type, "name": tag_name})
            pos = consume(html, pos, TAG_END)
        else:
            text, pos = consume_text(html, pos)
            tokens.append({"type": TEXT_TAG_TYPE, "data": text})
    return tokens


def consume_text(html: str, pos: int) -> tuple[str, int]:
    start = pos
    while pos < len(html) and html[pos] != TAG_START:
        pos += 1
    text = html[start:pos]
    return text, pos


def consume_tag_name(html: str, pos: int) -> tuple[str, str, dict | None, int]:
    # <a12> the current position expected at a., traverse until we find > (END_TAG)
    # First, we need to check, the tag type.
    if pos >= len(html):
        raise ValueError("Unexpected end of the html document")
    tag_type = START_TAG_TYPE
    if html[pos] == "/":
        tag_type = END_TAG_TYPE
        pos += 1
    start = pos
    while (
        pos < len(html)
        and html[pos] != TAG_END  # no attributes
        and html[pos] != " "  # has attributes (or just spaces)
        and html[pos] != "/"  # self closing tag.
    ):
        pos += 1

    tag_name = html[start:pos]
    if pos < len(html) and html[pos] == "/":  # self closing.
        tag_type = SELF_CLOSING_TAG_TYPE
        pos += 1
    # validate tag name.
    if not TAG_PATTERN.fullmatch(tag_name):
        raise ValueError("Invalid tag name")

    # consume attributes here.
    pos = consume_whitespaces(html, pos)
    if pos < len(html) and html[pos] == TAG_END:
        return tag_name, tag_type, None, pos
    attrs, pos = consume_attributes(html, pos)
    if pos < len(html) and html[pos] == "/":
        tag_type = SELF_CLOSING_TAG_TYPE
        pos += 1
    return tag_name, tag_type, attrs, pos


def consume_attributes(html: str, pos: int) -> tuple[Attributes, int]:
    attrs = {}
    while pos < len(html) and html[pos] != TAG_END and html[pos] != "/":
        attr_name, pos = consume_attr_name(html, pos)
        pos = consume(html, pos, "=")
        pos = consume(html, pos, '"')
        attr_val, pos = consume_attr_value(html, pos)
        pos = consume(html, pos, '"')
        pos = consume_whitespaces(html, pos)
        attrs[attr_name] = attr_val
    return attrs, pos


def consume_attr_name(html: str, pos: int) -> tuple[str, int]:
    start = pos
    while pos < len(html) and html[pos] != "=":
        pos += 1
    attr_name = html[start:pos]
    if not ATTR_PATTERN.fullmatch(attr_name):
        raise ValueError("Invalid attribute value name")
    return attr_name, pos


def consume_attr_value(html: str, pos: int) -> tuple[str, int]:
    start = pos
    while pos < len(html) and html[pos] != '"':
        pos += 1
    attr_val = html[start:pos]
    return attr_val, pos


def consume_whitespaces(html: str, pos: int) -> int:
    while (
        pos < len(html) and html[pos].isspace()
    ):  # handle all white space characters. (just space, line break etc)
        pos += 1
    return pos


def consume(html: str, pos: int, pattern: str) -> int:
    if not html[pos:].startswith(pattern):
        raise ValueError("Unexpected data. The pattern is not found.")
    pos += len(pattern)
    return pos


def parse(tokens: Tokens) -> ElementNode:
    root = ElementNode("root")
    stack = [root]
    for t in tokens:
        token_type = t.get("type")
        if not token_type:
            raise ValueError("type field is required")
        if token_type == START_TAG_TYPE:
            name = t.get("name")
            if not name:
                raise ValueError("name is required for the start tag.")
            new_node = ElementNode(name, t.get("attrs", {}))
            stack.append(new_node)
        elif token_type == SELF_CLOSING_TAG_TYPE:
            # build a new node, add to the child of the current head.
            name = t.get("name")
            if not name:
                raise ValueError("name is required for the self-closing tag.")
            new_node = ElementNode(name, t.get("attrs", {}))
            stack[-1].children.append(new_node)
        elif token_type == END_TAG_TYPE:
            # pop the last node, add to the parent node child
            poped = stack.pop()
            stack[-1].children.append(poped)
        elif token_type == TEXT_TAG_TYPE:
            # build a text node. add to the current head node children.
            data = t.get("data")
            if not data:
                raise ValueError("data is required for the text element.")
            new_node = TextNode(data)
            stack[-1].children.append(new_node)
        else:
            raise ValueError("unsupproted tag type")
    return root
