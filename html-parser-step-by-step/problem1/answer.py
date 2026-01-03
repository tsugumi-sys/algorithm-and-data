import re

TOKEN_START = "<"
TOKEN_END = ">"

TAG_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")


def tokenize(html: str) -> list[dict[str, str]]:
    pos = 0
    tokens = []

    while pos < len(html):
        if html[pos] == "<":
            # consume tag name. (check type, start or end)
            token_type, tag_name, pos = consume_tag(html, pos)
            pos = consume(html, TOKEN_END, pos)
            tokens.append({"type": token_type, "name": tag_name})
        else:
            token_type, text, pos = consume_text(html, pos)
            tokens.append({"type": token_type, "data": text})
    return tokens


def consume_text(html: str, pos: int) -> tuple[str, str, int]:
    start = pos
    while pos < len(html) and html[pos] != TOKEN_START:
        pos += 1
    return "Text", html[start:pos], pos


def consume_tag(
    html: str, pos: int
) -> tuple[str, str, int]:  # type, tag name, position.
    if html[pos] != TOKEN_START:
        raise ValueError("Unexpected tar start")

    pos += 1
    start = pos
    while pos < len(html) and html[pos] != TOKEN_END:
        pos += 1

    is_end_tag = False
    tag_name = html[start:pos]
    if tag_name.startswith("/"):
        is_end_tag = True
        tag_name = tag_name[1:]
    if not TAG_PATTERN.fullmatch(tag_name):
        raise ValueError("Invalid tag name")
    return ("EndTag" if is_end_tag else "StartTag", tag_name, pos)


def consume(html: str, pattern: str, pos: int) -> int:
    if not html[pos:].startswith(pattern):
        raise ValueError("Unexpected input")
    pos += len(pattern)
    return pos
