## Problem 1: Separate token types cleanly

### Goal

Instead of a sloppy tuple like `('TAG', 'div')`,  
instead of a sloppy tuple, produce a token list that clearly distinguishes  
**StartTag / EndTag / Text**.

### Requirements

* The output should be a dict (or dataclass) like this:

```python
{"type": "StartTag", "name": "div"}
{"type": "EndTag", "name": "div"}
{"type": "Text", "data": "Hello"}
```

### Examples

```python
tokenize("<div>Hello</div>")
# -> [
#   {"type": "StartTag", "name": "div"},
#   {"type": "Text", "data": "Hello"},
#   {"type": "EndTag", "name": "div"},
# ]

tokenize("A<br>B")
# -> [
#   {"type": "Text", "data": "A"},
#   {"type": "StartTag", "name": "br"},
#   {"type": "Text", "data": "B"},
# ]
```

### Hint

* You can split Start/End by whether the `TAG` string starts with `/`

  * Example: `"div"` → StartTag, `"/div"` → EndTag
