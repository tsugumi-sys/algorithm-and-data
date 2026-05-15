// Exercise 3: Check whether a string is a palindrome.
//
// Run:
// rustc --edition=2021 --test 03_palindrome_check.rs && ./03_palindrome_check

fn is_palindrome(s: &str) -> bool {
    let normalized: String = s
        .chars()
        .filter(|ch| !ch.is_whitespace())
        .flat_map(|ch| ch.to_lowercase())
        .collect();

    normalized.chars().eq(normalized.chars().rev())
}

fn main() {
    println!("{}", is_palindrome("Never odd or even"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn detects_simple_palindrome() {
        assert!(is_palindrome("level"));
    }

    #[test]
    fn ignores_case_and_spaces() {
        assert!(is_palindrome("Never odd or even"));
    }

    #[test]
    fn rejects_non_palindrome() {
        assert!(!is_palindrome("rust"));
    }
}
