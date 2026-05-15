// Exercise 4: Count how many times each word appears.
//
// Run:
// rustc --edition=2021 --test 04_word_frequency.rs && ./04_word_frequency

use std::collections::HashMap;

fn word_frequency(s: &str) -> HashMap<String, usize> {
    let mut counter = HashMap::new();
    for w in s.split_whitespace() {
        *counter.entry(w.to_lowercase().to_string()).or_insert(0) += 1;
    }
    counter
}

fn main() {
    println!("{:?}", word_frequency("Rust rust language"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn counts_words_case_insensitively() {
        let map = word_frequency("Rust rust language");

        assert_eq!(map.get("rust"), Some(&2));
        assert_eq!(map.get("language"), Some(&1));
    }

    #[test]
    fn handles_extra_spaces() {
        let map = word_frequency("  one   two one  ");

        assert_eq!(map.get("one"), Some(&2));
        assert_eq!(map.get("two"), Some(&1));
        assert_eq!(map.len(), 2);
    }

    #[test]
    fn empty_string_returns_empty_map() {
        assert!(word_frequency("").is_empty());
    }
}
