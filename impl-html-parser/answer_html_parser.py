"""
Reference implementation of a minimal HTML parser to match the README contract.

Supported:
- Lowercase tag names [a-z]+
- Attributes key="value" (double quotes only), preserving insertion order
- Start tags, end tags, and self-closing tags (<tag .../>)
- Text nodes preserve whitespace as-is

Raises ValueError for malformed input in this subset or unsupported constructs.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import re


# Limited grammars keep the parser small and deterministic for the toy subset.
TAG_RE = re.compile(r"[a-z]+")
ATTR_NAME_RE = re.compile(r"[a-z][a-z0-9_-]*")


@dataclass
class Node:
    type: str
    tag: Optional[str] = None
    attributes: Dict[str, str] = field(default_factory=dict)
    children: List["Node"] = field(default_factory=list)
    text: Optional[str] = None


class HTMLParser:
    def parse(self, html: str) -> Node:
        self.html = html
        self.pos = 0
        self.length = len(html)
        root = Node(type="document", tag=None, attributes={}, children=[])
        stack: List[Node] = [root]

        while self.pos < self.length:
            if self._peek() == "<":
                # Reject any markup we explicitly exclude (comments, doctypes, etc.).
                if self._peek(1) == "!":
                    raise ValueError("Unsupported construct")
                if self._peek(1) == "?":
                    raise ValueError("Unsupported construct")
                if self._peek(1) == "/":
                    # Closing tag: must match the most recent open element.
                    self._consume("</")
                    tag = self._parse_tag_name()
                    self._consume_whitespace()
                    if not self._match(">"):
                        raise ValueError("Expected '>' for closing tag")
                    self._consume(">")
                    if len(stack) == 1:
                        raise ValueError("Unexpected closing tag")
                    open_node = stack.pop()
                    if open_node.tag != tag:
                        raise ValueError("Mismatched closing tag")
                else:
                    # Start tag (possibly self-closing) with attributes.
                    self._consume("<")
                    tag = self._parse_tag_name()
                    attributes = self._parse_attributes()
                    self._consume_whitespace()
                    self_closing = False
                    if self._match("/>"):
                        self_closing = True
                        self._consume("/>")
                    elif self._match(">"):
                        self._consume(">")
                    else:
                        raise ValueError("Expected '>' to close start tag")

                    node = Node(
                        type="element", tag=tag, attributes=attributes, children=[]
                    )
                    stack[-1].children.append(node)
                    if not self_closing:
                        stack.append(node)
            else:
                # Text runs become their own nodes; whitespace is preserved.
                text = self._consume_text()
                if text:
                    stack[-1].children.append(
                        Node(type="text", tag=None, attributes={}, children=[], text=text)
                    )

        if len(stack) != 1:
            raise ValueError("Unclosed tag at end of input")
        return root

    def _consume_text(self) -> str:
        # Consume until the next '<' (start of markup) to keep text contiguous.
        start = self.pos
        while self.pos < self.length and self.html[self.pos] != "<":
            self.pos += 1
        return self.html[start : self.pos]

    def _parse_tag_name(self) -> str:
        # Tags are lowercase alpha only per the limited grammar.
        start = self.pos
        while self.pos < self.length and self.html[self.pos].isalpha():
            self.pos += 1
        name = self.html[start : self.pos]
        if not name or not TAG_RE.fullmatch(name):
            raise ValueError("Invalid tag name")
        return name

    def _parse_attributes(self) -> Dict[str, str]:
        # Parse key="value" pairs, preserving insertion order.
        attrs: Dict[str, str] = {}
        while True:
            self._consume_whitespace()
            if self._peek() in (">", "/") or self.pos >= self.length:
                break
            name = self._parse_attribute_name()
            self._consume_whitespace()
            if not self._match("="):
                raise ValueError("Expected '=' after attribute name")
            self._consume("=")
            self._consume_whitespace()
            if not self._match('"'):
                raise ValueError("Attribute values must use double quotes")
            self._consume('"')
            value_start = self.pos
            while self.pos < self.length and self.html[self.pos] != '"':
                self.pos += 1
            if self.pos >= self.length:
                raise ValueError("Unterminated attribute value")
            value = self.html[value_start : self.pos]
            self._consume('"')
            attrs[name] = value
        return attrs

    def _parse_attribute_name(self) -> str:
        # Attribute names follow the limited lowercase/digit/underscore/dash rule.
        start = self.pos
        while (
            self.pos < self.length
            and (self.html[self.pos].isalnum() or self.html[self.pos] in "_-")
        ):
            self.pos += 1
        name = self.html[start : self.pos]
        if not name or not ATTR_NAME_RE.fullmatch(name):
            raise ValueError("Invalid attribute name")
        return name

    def _consume_whitespace(self) -> None:
        while self.pos < self.length and self.html[self.pos].isspace():
            self.pos += 1

    def _match(self, s: str) -> bool:
        return self.html.startswith(s, self.pos)

    def _consume(self, s: str) -> None:
        if not self.html.startswith(s, self.pos):
            raise ValueError("Unexpected input")
        self.pos += len(s)

    def _peek(self, offset: int = 0) -> str:
        idx = self.pos + offset
        if idx >= self.length:
            return ""
        return self.html[idx]
