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
