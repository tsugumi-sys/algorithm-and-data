## Problem 5 (challenge): Tolerate broken HTML

### Goal

Even with input like this, build a reasonable tree:

```html
<div><b>bold</div>
```

Ideal behavior (one example):

```text
Element(div)
  └─ Element(b)
        └─ Text("bold")
```

In other words:

* When you see `</div>`, close up to the nearest matching start tag (`<div>`)
* Allow `<b>` to be left unclosed

This is **a bit closer to browser behavior**.
