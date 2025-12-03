## 🧱 前提：Problem 0（今やろうとしてるやつ）

**Problem 0: 一番シンプルな Tokenizer**

* **入力**: `str`（HTMLライクな文字列）
* **出力**: `list[tuple[str, str]]`

  * `('TAG', 'div')`
  * `('TEXT', 'Hello')`
  * `('TAG', '/div')`

### 仕様

* `<` が来たら「タグ開始」、`>` までを `TAG` として読む
* それ以外は `TEXT` として読む
* 階層構造は考えない（ただの列）

### 入出力例

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
