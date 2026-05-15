// Exercise 5: Group words by their first char.
//
// Run:
// rustc --edition=2021 --test 05_group_words_by_first_char.rs && ./05_group_words_by_first_char

use std::collections::HashMap;

fn group_words_by_first_char(s: &str) -> HashMap<char, Vec<String>> {
    let mut groups = HashMap::new();
    for w in s.split_whitespace() {
        if let Some(head) = w.chars().next() {
            groups.entry(head).or_insert(Vec::new()).push(w.to_string());
        }
    }
    groups
}

fn main() {
    println!("{:?}", group_words_by_first_char("apple banana apricot"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn groups_words_by_first_char() {
        let map = group_words_by_first_char("apple banana apricot");

        assert_eq!(
            map.get(&'a'),
            Some(&vec!["apple".to_string(), "apricot".to_string()])
        );
        assert_eq!(map.get(&'b'), Some(&vec!["banana".to_string()]));
    }

    #[test]
    fn handles_unicode_words() {
        let map = group_words_by_first_char("あお あか いえ");

        assert_eq!(
            map.get(&'あ'),
            Some(&vec!["あお".to_string(), "あか".to_string()])
        );
        assert_eq!(map.get(&'い'), Some(&vec!["いえ".to_string()]));
    }

    #[test]
    fn empty_string_returns_empty_map() {
        assert!(group_words_by_first_char("").is_empty());
    }
}
