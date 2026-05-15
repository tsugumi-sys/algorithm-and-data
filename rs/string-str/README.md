## String / &str in Rust

Rust の文字列は所有権、借用、UTF-8 が絡むため、`String` と `&str` の使い分けに早めに慣れる。

各ファイルは `todo!()` を埋めて、テストが通るように実装する。

実行例:

```sh
rustc --edition=2021 --test 01_reverse_words.rs && ./01_reverse_words
```

## 1. reverse words

File: `01_reverse_words.rs`

文字列を単語ごとに分割し、単語の順番だけを逆にして結合する練習。

Goal:

- 引数は `&str` で受け取る
- 返り値は所有権を持つ `String` にする
- 余分な空白は `split_whitespace()` でまとめて扱う

## 2. count chars

File: `02_count_chars.rs`

Rust の文字列は UTF-8 なので、バイト数と文字数が一致しない場合がある。
`.chars()` を使って Unicode scalar value の数を数える練習。

Goal:

- `&str` の文字数を返す
- ASCII と日本語の両方で動くことを確認する
- `.len()` との違いを意識する

## 3. palindrome check

File: `03_palindrome_check.rs`

前から読んでも後ろから読んでも同じ文字列かを判定する練習。

Goal:

- 英字の大文字小文字を無視する
- 空白は無視する
- `chars()` と `rev()` を使う

## 4. split and join

File: `04_split_join.rs`

区切り文字で分割し、空要素を除いたうえで別の区切り文字で結合する練習。

Goal:

- `&str` を `split()` で分割する
- 空要素を除外する
- `Vec<&str>` と `join()` を使う

## 5. word frequency count

File: `05_word_frequency.rs`

単語の出現回数を `HashMap` で数える練習。

Goal:

- `&str` を受け取る
- 小文字化してから数える
- 返り値は `HashMap<String, usize>` にする
