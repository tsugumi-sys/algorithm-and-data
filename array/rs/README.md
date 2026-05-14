## Array in Rust

Basic array operations in Rust.

## Next Exercises

配列とスライスで次に押さえるポイントを、1項目1ファイルで練習します。
各ファイルは `todo!()` を埋めて、テストが通るように実装します。

実行例:

```sh
rustc --edition=2021 --test 01_slice_args.rs && ./01_slice_args
```

## 1. 配列とスライスの使い分け

File: `01_slice_args.rs`

固定長配列 `[T; N]` と可変長の `Vec<T>` の両方を、関数引数 `&[T]` として受け取る練習です。
Rust では、読み取りだけなら具体的な配列型よりスライスを受ける設計がよく使われます。

スライスは配列やvecの一部分をコピーせず参照するためのビュー。

Goal:

- `&[i32]` を受け取って合計値を返す
- 配列と `Vec<i32>` のどちらでも同じ関数を呼べることを確認する

## 2. `iter` / `iter_mut` / `into_iter`

File: `02_iter_variants.rs`

参照で読む、可変参照で変更する、所有権を消費して値を取り出す、という3つの違いを練習します。

Goal:

- `iter()` で合計を計算する
- `iter_mut()` で各要素を2倍にする
- `into_iter()` で `String` 配列から `Vec<String>` を作る

## 3. 安全なアクセス: `get`

File: `03_safe_get.rs`

`array[index]` は範囲外で panic します。
`get()` を使うと `Option<&T>` として安全に扱えます。

Goal:

- 指定した index の値を返す
- 範囲外なら `None` を返す
- `Option` を使って panic しないコードを書く

## 4. 部分配列処理: `windows` / `chunks`

File: `04_windows_chunks.rs`

隣接要素の比較や、一定サイズごとの処理でよく使う API です。

Goal:

- `windows(2)` で隣同士の差分を作る
- `chunks(n)` で区切った各グループの合計を作る

## 5. `Vec` を使う場面

File: `05_vec_basics.rs`

サイズが実行時に変わるデータは、固定長配列ではなく `Vec<T>` を使います。

Goal:

- `Vec` に条件を満たす値だけ追加する
- `push` と `len` の基本を確認する
- 配列から `Vec` を作る

## 6. ソートの派生

File: `06_sort_variants.rs`

`sort()` の次に、降順ソートやキー指定ソートを練習します。

Goal:

- 数値を降順に並べる
- 文字列を長さ順に並べる
- タプルを2番目の値で並べる
