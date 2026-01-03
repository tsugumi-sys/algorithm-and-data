## Problem 1: Token 型をちゃんと分ける

### ゴール

`('TAG', 'div')` みたいな雑なタプルじゃなくて、  
**StartTag / EndTag / Text** をきちんと区別したトークン列にする。

### 要件

* 出力はこんな感じの dict（or dataclass）にする：

```python
{"type": "StartTag", "name": "div"}
{"type": "EndTag", "name": "div"}
{"type": "Text", "data": "Hello"}
```

### 入出力例

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

### ヒント

* `TAG` 文字列が `/` から始まるかで Start/End を分けられる

  * 例: `"div"` → StartTag, `"/div"` → EndTag
