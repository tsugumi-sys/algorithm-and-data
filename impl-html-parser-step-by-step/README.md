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

---

ここから発展問題いくよ 👇

---

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

---

## Problem 2: 属性付きタグに対応する（でもまだフラット）

### ゴール

タグの属性をパースしてみる。

```html
<div id="main" class="c1 c2">Hello</div>
```

をこんなトークンにしたい：

```python
{"type": "StartTag", "name": "div", "attrs": {"id": "main", "class": "c1 c2"}}
{"type": "Text", "data": "Hello"}
{"type": "EndTag", "name": "div"}
```

### 要件（シンプルでOK）

* 属性は `name="value"` 形式のみ対応
* シングルクォート `'` は考えなくていい（ダブルクォート限定）
* 値にスペースは含まれてもいい（`class="c1 c2"` など）
* 属性同士はスペース区切り

### 入出力例

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

### ヒント

* `TAG` 文字列を `name` 部分と `attr` 部分に分割するイメージ

  * 先頭の単語 → タグ名
  * それ以降をパースして `name="value"` を取る
* 正規表現を使ってもいいし、素直に state machine でもOK

---

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

### 要件

* 入力は**正しいネスト**を仮定（壊れたHTMLは考えない）
* `StartTag`：新しい `ElementNode` を作ってスタックに積む
* `Text`：スタックの一番上の `children` に追加
* `EndTag`：スタックから Pop して、一つ上の `children` に追加
* 一番外側は `root` ノードを作ってぶら下げてもいい

---

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

---

## Problem 5（チャレンジ）: 壊れたHTMLへの耐性

### ゴール

次みたいな入力でも、とりあえずそれっぽくツリーを作る：

```html
<div><b>bold</div>
```

理想的な挙動（一例）：

```text
Element(div)
  └─ Element(b)
        └─ Text("bold")
```

つまり：

* `</div>` を見たときに、一番近い対応するStartTag（`<div>`）まで閉じる
* `<b>` が閉じられてなくても許す

これは **ブラウザの挙動にちょっと近づく感じ**。
