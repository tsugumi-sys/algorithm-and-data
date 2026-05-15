// Exercise 2: Check whether `s` contains all chars in `required`.
//
// Run:
// rustc --edition=2021 --test 02_contains_all_chars.rs && ./02_contains_all_chars

use std::collections::HashSet;

fn contains_all_chars(s: &str, required: &str) -> bool {
    let mut chars = HashSet::new();
    for ch in s.chars() {
        chars.insert(ch);
    }
    for ch in required.chars() {
        if !chars.contains(&ch) {
            return false;
        }
    }
    true
}

fn main() {
    println!("{}", contains_all_chars("banana", "ban"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_true_when_all_chars_exist() {
        assert!(contains_all_chars("banana", "ban"));
    }

    #[test]
    fn returns_false_when_a_char_is_missing() {
        assert!(!contains_all_chars("banana", "cat"));
    }

    #[test]
    fn ignores_duplicate_required_chars() {
        assert!(contains_all_chars("banana", "aaa"));
    }

    #[test]
    fn empty_required_is_true() {
        assert!(contains_all_chars("banana", ""));
    }
}
