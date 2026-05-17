// Exercise 1: Check whether parentheses are valid.
//
// Run:
// rustc --edition=2021 --test 01_valid_parentheses.rs && ./01_valid_parentheses

#![allow(unused)]

use std::collections::HashMap;

fn is_valid_parentheses(s: &str) -> bool {
    let mut tags: HashMap<char, char> = [('(', ')'), ('[', ']'), ('{', '}')].into_iter().collect();
    let mut stack = Vec::new();
    for ch in s.chars() {
        if let Some(&close) = tags.get(&ch) {
            stack.push(close);
        } else {
            if stack.is_empty() {
                return false;
            }
            if let Some(poped) = stack.pop() {
                if poped != ch {
                    return false;
                }
            }
        }
    }
    stack.is_empty()
}

fn main() {
    println!("{}", is_valid_parentheses("({[]})"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn accepts_balanced_parentheses() {
        assert!(is_valid_parentheses("()"));
        assert!(is_valid_parentheses("({[]})"));
        assert!(is_valid_parentheses("()[{}]"));
    }

    #[test]
    fn rejects_mismatched_parentheses() {
        assert!(!is_valid_parentheses("(]"));
        assert!(!is_valid_parentheses("([)]"));
        assert!(!is_valid_parentheses("((()"));
    }

    #[test]
    fn accepts_empty_string() {
        assert!(is_valid_parentheses(""));
    }
}
