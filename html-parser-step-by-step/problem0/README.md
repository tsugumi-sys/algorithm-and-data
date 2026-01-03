## Prereq: Problem 0 (what you're about to do)

**Problem 0: The simplest tokenizer**

* **Input**: `str` (HTML-like string)
* **Output**: `list[tuple[str, str]]`

  * `('TAG', 'div')`
  * `('TEXT', 'Hello')`
  * `('TAG', '/div')`

### Specs

* When you see `<`, treat it as "tag start" and read until `>` as `TAG`
* Otherwise read as `TEXT`
* Do not consider nesting (just a flat list)

### Examples

```python
tokenize("<div>Hello</div>")
# -> [('TAG', 'div'), ('TEXT', 'Hello'), ('TAG', '/div')]

tokenize("Hi<br>there")
# -> [('TEXT', 'Hi'), ('TAG', 'br'), ('TEXT', 'there')]

tokenize("<p>A <b>bold</b> move</p>")
# -> [
#   ('TAG', 'p'),
#   ('TEXT', 'A '),
#   ('TAG', 'b'),
#   ('TEXT', 'bold'),
#   ('TAG', '/b'),
#   ('TEXT', ' move'),
#   ('TAG', '/p'),
# ]
```
