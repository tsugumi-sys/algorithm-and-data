// Exercise 1: Reverse the order of words in a string.
//
// Run:
// rustc --edition=2021 --test 01_reverse_words.rs && ./01_reverse_words

fn reverse_words(s: &str) -> String {
    // deref -> reverse
    let mut words: Vec<&str> = s.split_whitespace().collect();
    words.reverse();
    words.join(" ")
}

fn main() {
    println!("{}", reverse_words("hello from rust"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn reverses_words() {
        assert_eq!(reverse_words("hello from rust"), "rust from hello");
    }

    #[test]
    fn collapses_extra_spaces() {
        assert_eq!(reverse_words("  hello   rust  "), "rust hello");
    }

    #[test]
    fn empty_string_returns_empty_string() {
        assert_eq!(reverse_words(""), "");
    }
}
