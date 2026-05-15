## HashMap / HashSet in Rust

`HashSet` と `HashMap` の基本操作に慣れるための練習。

各ファイルは `todo!()` を埋めて、テストが通るように実装する。

実行例:

```sh
rustc --edition=2021 --test 01_unique_chars.rs && ./01_unique_chars
```

## 1. unique chars

File: `01_unique_chars.rs`

文字列に含まれる文字を重複なしで取り出す練習。

Goal:

- `HashSet<char>` を返す
- `chars()` と `collect()` を使う
- 重複した文字が1つにまとまることを確認する

## 2. contains all chars

File: `02_contains_all_chars.rs`

ある文字列が、別の文字列に含まれる文字をすべて持っているか判定する練習。

Goal:

- `HashSet<char>` を使って membership check をする
- `contains()` を使う
- 空文字の場合も自然に扱う

## 3. char frequency

File: `03_char_frequency.rs`

文字ごとの出現回数を数える練習。

Goal:

- `HashMap<char, usize>` を返す
- `entry(...).or_insert(...)` を使う
- 同じ文字が出たらカウントを増やす

## 4. word frequency

File: `04_word_frequency.rs`

単語ごとの出現回数を数える練習。

Goal:

- `HashMap<String, usize>` を返す
- `split_whitespace()` を使う
- 小文字化してから数える

## 5. group words by first char

File: `05_group_words_by_first_char.rs`

単語を先頭文字ごとにグルーピングする練習。

Goal:

- `HashMap<char, Vec<String>>` を返す
- `entry(...).or_insert_with(Vec::new)` を使う
- 空白だけの入力を扱う
