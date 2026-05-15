// Exercise 1: Return unique chars in a string.
//
// Run:
// rustc --edition=2021 --test 01_unique_chars.rs && ./01_unique_chars

use std::collections::HashSet;

fn unique_chars(s: &str) -> HashSet<char> {
    let mut chars = HashSet::new();
    for s in s.chars().collect::<Vec<_>>() {
        chars.insert(s);
    }
    chars
}

fn main() {
    println!("{:?}", unique_chars("banana"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn removes_duplicates() {
        let set = unique_chars("banana");

        assert_eq!(set.len(), 3);
        assert!(set.contains(&'b'));
        assert!(set.contains(&'a'));
        assert!(set.contains(&'n'));
    }

    #[test]
    fn handles_unicode() {
        let set = unique_chars("あいうあ");

        assert_eq!(set.len(), 3);
        assert!(set.contains(&'あ'));
        assert!(set.contains(&'い'));
        assert!(set.contains(&'う'));
    }

    #[test]
    fn handles_empty_string() {
        assert!(unique_chars("").is_empty());
    }
}
