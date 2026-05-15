// Exercise 2: Count characters in a UTF-8 string.
//
// Run:
// rustc --edition=2021 --test 02_count_chars.rs && ./02_count_chars

fn count_chars(s: &str) -> usize {
    s.chars().count()
}

fn main() {
    println!("{}", count_chars("hello"));
    println!("{}", count_chars("こんにちは"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn counts_ascii_chars() {
        assert_eq!(count_chars("hello"), 5);
    }

    #[test]
    fn counts_japanese_chars() {
        assert_eq!(count_chars("こんにちは"), 5);
    }

    #[test]
    fn empty_string_is_zero() {
        assert_eq!(count_chars(""), 0);
    }
}
