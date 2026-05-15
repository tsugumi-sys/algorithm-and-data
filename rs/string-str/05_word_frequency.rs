// Exercise 5: Count word frequencies with HashMap.
//
// Run:
// rustc --edition=2021 --test 05_word_frequency.rs && ./05_word_frequency

use std::collections::HashMap;

fn word_frequency(s: &str) -> HashMap<String, usize> {
    let mut hashmap = HashMap::new();
    for word in s.split_whitespace() {
        let word = word.to_lowercase();
        *hashmap.entry(word).or_insert(0) += 1
    }
    hashmap
}

fn main() {
    println!("{:?}", word_frequency("Rust rust borrow"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn counts_words() {
        let counts = word_frequency("rust is fun rust");

        assert_eq!(counts.get("rust"), Some(&2));
        assert_eq!(counts.get("is"), Some(&1));
        assert_eq!(counts.get("fun"), Some(&1));
    }

    #[test]
    fn ignores_case() {
        let counts = word_frequency("Rust rust RUST");

        assert_eq!(counts.get("rust"), Some(&3));
        assert_eq!(counts.len(), 1);
    }

    #[test]
    fn empty_string_returns_empty_map() {
        let counts = word_frequency("");

        assert!(counts.is_empty());
    }
}
