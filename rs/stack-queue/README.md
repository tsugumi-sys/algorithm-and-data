## Stack / Queue in Rust

`Vec` を stack として使う操作と、`VecDeque` を queue として使う操作に慣れるための練習。

各ファイルは `todo!()` を埋めて、テストが通るように実装する。

実行例:

```sh
rustc --edition=2021 --test 01_valid_parentheses.rs && ./01_valid_parentheses
```

## 1. valid parentheses

File: `01_valid_parentheses.rs`

括弧列が正しく対応しているかを判定する練習。

Goal:

- `Vec<char>` を stack として使う
- `push()` と `pop()` を使う
- `()`, `{}`, `[]` の3種類を扱う

## 2. next greater element

File: `02_next_greater_element.rs`

各要素について、右側にある最初のより大きい値を探す練習。

Goal:

- index を stack に積む
- 見つからない場合は `-1` を返す
- `Vec<i32>` を返す

## 3. min stack

File: `03_min_stack.rs`

現在の最小値を `O(1)` で取り出せる stack を実装する練習。

Goal:

- `push`, `pop`, `top`, `get_min` を実装する
- 値用 stack と最小値用 stack を持つ
- 空の場合は `Option<i32>` を返す

## 4. queue with VecDeque

File: `04_queue_with_vecdeque.rs`

`VecDeque` を使って FIFO queue を実装する練習。

Goal:

- `push_back()` で enqueue する
- `pop_front()` で dequeue する
- `front()` と `len()` を実装する

## 5. simple BFS preparation

File: `05_simple_bfs.rs`

隣接リストで表した graph を、開始ノードから BFS で訪問する練習。

Goal:

- `VecDeque<usize>` を queue として使う
- `Vec<bool>` で訪問済みを管理する
- 訪問順を `Vec<usize>` で返す
