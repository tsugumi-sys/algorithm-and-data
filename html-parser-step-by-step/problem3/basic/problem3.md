## Problem 3: ネスト対応パーサー（DOMっぽいツリー作成）

ここから **「パーサー」** の領域。

### ゴール

Problem 1 or 2 で作ったトークン列から、  
**ツリー構造をもつノード** を生成する。

### Nodeのイメージ

Pythonだとこんなクラスを想定：

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

### 入力トークン例

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

### 出力ツリー（概念）

```text
ElementNode("div")
  ├─ TextNode("Hi ")
  └─ ElementNode("b")
        └─ TextNode("there")
```

### ヒント

* 入力は**正しいネスト**を仮定（壊れたHTMLは考えない）
* `StartTag`：新しい `ElementNode` を作ってスタックに積む
* `Text`：スタックの一番上の `children` に追加
* `EndTag`：スタックから Pop して、一つ上の `children` に追加
* 一番外側は `root` ノードを作ってぶら下げてもいい
