## Problem 4: Support self-closing tags (`<br/>`, `<img />`)

### Goal

Treat self-closing tags as a Start→End pair.

```html
<div>Hello<br/>World</div>
```

Parsed tree:

```text
Element(div)
  ├─ Text("Hello")
  ├─ Element(br)
  └─ Text("World")
```

### Requirements

* In the tokenizer, when you see `<br/>`,
  it's OK to emit `{"type": "SelfClosingTag", "name": "br"}`
* In the parser, when you see `SelfClosingTag`:

  * Create a single `ElementNode` with no children, and **do not touch the stack**
