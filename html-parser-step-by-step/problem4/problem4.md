## Problem 4: self-closing タグに対応（`<br/>`, `<img />`）

### ゴール

Self-closing タグを「Start→End のセット」として扱う。

```html
<div>Hello<br/>World</div>
```

をパースした結果ツリー：

```text
Element(div)
  ├─ Text("Hello")
  ├─ Element(br)
  └─ Text("World")
```

### 要件

* Tokenizer側で `<br/>` を見たら
  → `{"type": "SelfClosingTag", "name": "br"}` としてもOK
* Parser側で `SelfClosingTag` を見たら：

  * 子要素なしの `ElementNode` をひとつ作り、**スタック操作はしない**
