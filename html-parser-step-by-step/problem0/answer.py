TAG_START = "<"
TAG_END = ">"


def tokenize(html: str) -> list[tuple[str, str]]:
    pos = 0
    tags = []

    while pos < len(html):
        if html[pos] == TAG_START:
            consumed, pos = consume_tag(html, pos)
            pos = consume(html, TAG_END, pos)
            tags.append(("TAG", consumed))
        else:
            consumed, pos = consume_text(html, pos)
            tags.append(("TEXT", consumed))
    return tags


def consume_tag(html: str, pos: int) -> tuple[str, int]:
    if pos < 0:
        raise ValueError()

    if html[pos] != TAG_START:
        raise ValueError("Unexpected Input")

    pos += 1
    start = pos
    if html[start] != "/" and not html[start].isalpha():
        raise ValueError("Invalid tag name")
    while pos < len(html) and html[pos] != TAG_END:
        pos += 1
    tag_name = html[start:pos]
    return tag_name, pos


def consume_text(html: str, pos: int) -> tuple[str, int]:
    if pos < 0:
        raise ValueError()

    start = pos
    while pos < len(html) and html[pos] != TAG_START:  # tag starting.
        pos += 1
    return html[start:pos], pos


def consume(html: str, target: str, pos: int) -> int:
    if not html[pos:].startswith(target):
        raise ValueError("Unexpected input")
    pos += len(target)
    return pos
