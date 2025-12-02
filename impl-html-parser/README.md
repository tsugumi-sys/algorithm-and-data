Simple HTML parser requirements (intentionally limited)

- Provide a `Node` type with these fields: `type` (`"document"`, `"element"`, `"text"`), `tag` (str or None), `attributes` (dict), `children` (list of `Node`), and `text` (str or None). Document nodes have `type="document"` and hold top-level children; text nodes carry their `text` value and no children.
- Expose an `HTMLParser` class with `parse(html: str) -> Node` that returns a document node representing the input fragment; the parser should not normalize whitespace and should preserve text exactly as written between tags.
- Supported tags: lowercase names made of `[a-z]+`; start tags `<tag ...>`, end tags `</tag>`, and self-closing tags `<tag .../>` (which never have children).
- Supported attributes: zero or more per element, written as `key="value"` (double quotes only); attribute order must be preserved in the original dict insertion order.
- Parsing behavior: build a tree that maintains the original order of child nodes (elements and text), create separate text nodes for each contiguous run of characters outside tags, and allow multiple sibling top-level elements under the document node.
- Error handling: raise `ValueError` for malformed HTML in this subset (unexpected closing tag, mismatched tags, missing closing tags at EOF, or unterminated attributes/tags).
- Out of scope (may raise `ValueError`): comments, doctypes, CDATA, scripts/styles with raw text rules, entity decoding, unquoted/boolean attributes, uppercase tags, and any tag/attribute names outside the limited character set.

Files to implement

- `html_parser.py`: implement `Node` and `HTMLParser` to satisfy the above tests.
- `test_html_parser.py`: pytest suite exercising the required behavior.
