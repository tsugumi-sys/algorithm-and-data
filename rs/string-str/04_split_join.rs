// Exercise 4: Split a string and join non-empty parts.
//
// Run:
// rustc --edition=2021 --test 04_split_join.rs && ./04_split_join

fn split_and_join(s: &str, from: char, to: &str) -> String {
    s.split(from)
        .filter(|w| !w.is_empty())
        .collect::<Vec<_>>()
        .join(to)
}

fn main() {
    println!("{}", split_and_join("red,,blue,green", ',', " | "));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn joins_with_new_separator() {
        assert_eq!(
            split_and_join("red,blue,green", ',', " | "),
            "red | blue | green"
        );
    }

    #[test]
    fn skips_empty_parts() {
        assert_eq!(split_and_join("red,,blue,", ',', "-"), "red-blue");
    }

    #[test]
    fn all_empty_parts_return_empty_string() {
        assert_eq!(split_and_join(",,,", ',', "-"), "");
    }
}
