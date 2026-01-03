## Problem 2: Support tags with attributes (still flat)

### Goal

Parse tag attributes.

```html
<div id="main" class="c1 c2">Hello</div>
```

into tokens like:

```python
{"type": "StartTag", "name": "div", "attrs": {"id": "main", "class": "c1 c2"}}
{"type": "Text", "data": "Hello"}
{"type": "EndTag", "name": "div"}
```

### Requirements (simple is fine)

* Only support attributes in `name="value"` form
* You can ignore single quotes `'` (double quotes only)
* Values may include spaces (e.g. `class="c1 c2"`)
* Attributes are separated by spaces

### Examples

```python
tokenize('<img src="a.png" alt="logo">')
# -> [
#   {
#     "type": "StartTag",
#     "name": "img",
#     "attrs": {"src": "a.png", "alt": "logo"},
#   }
# ]

tokenize('<a href="https://example.com">Link</a>')
# -> [
#   {"type": "StartTag", "name": "a", "attrs": {"href": "https://example.com"}},
#   {"type": "Text", "data": "Link"},
#   {"type": "EndTag", "name": "a"},
# ]
```

### Hint

* Split the `TAG` string into a `name` part and an `attr` part

  * First word → tag name
  * Parse the rest to extract `name="value"`
* Regex is fine, or a simple state machine
