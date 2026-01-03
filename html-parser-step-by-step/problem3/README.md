## Problem 3: Nested parser (build a DOM-like tree)

From here it's the **parser** part.

### Goal

From the token list built in Problem 1 or 2,  
generate **nodes with a tree structure**.

### Node shape

In Python, imagine classes like this:

```python
class ElementNode:
    def __init__(self, name, attrs=None, children=None):
        self.name = name
        self.attrs = attrs or {}
        self.children = children or []

class TextNode:
    def __init__(self, data):
        self.data = data
```

### Input token example

```python
tokens = [
  {"type": "StartTag", "name": "div"},
  {"type": "Text", "data": "Hi "},
  {"type": "StartTag", "name": "b"},
  {"type": "Text", "data": "there"},
  {"type": "EndTag", "name": "b"},
  {"type": "EndTag", "name": "div"},
]
```

### Output tree (conceptual)

```text
ElementNode("div")
  ├─ TextNode("Hi ")
  └─ ElementNode("b")
        └─ TextNode("there")
```

### Hint

* Assume the input is **properly nested** (ignore broken HTML)
* `StartTag`: create a new `ElementNode` and push it on the stack
* `Text`: append to the top stack node's `children`
* `EndTag`: pop from the stack and append to the parent node's `children`
* You can create an outer `root` node and attach everything to it
