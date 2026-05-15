// Exercise 3: Count how many times each char appears.
//
// Run:
// rustc --edition=2021 --test 03_char_frequency.rs && ./03_char_frequency

use std::collections::HashMap;

fn char_frequency(s: &str) -> HashMap<char, usize> {
    let mut counter = HashMap::new();
    for ch in s.chars() {
        *counter.entry(ch).or_insert(0) += 1;
    }
    counter
}

fn main() {
    println!("{:?}", char_frequency("banana"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn counts_ascii_chars() {
        let map = char_frequency("banana");

        assert_eq!(map.get(&'b'), Some(&1));
        assert_eq!(map.get(&'a'), Some(&3));
        assert_eq!(map.get(&'n'), Some(&2));
    }

    #[test]
    fn counts_unicode_chars() {
        let map = char_frequency("あいうあ");

        assert_eq!(map.get(&'あ'), Some(&2));
        assert_eq!(map.get(&'い'), Some(&1));
        assert_eq!(map.get(&'う'), Some(&1));
    }

    #[test]
    fn empty_string_returns_empty_map() {
        assert!(char_frequency("").is_empty());
    }
}
