// Exercise 6: Practice sort_by() and sort_by_key().
//
// Run:
// rustc --edition=2021 --test 06_sort_variants.rs && ./06_sort_variants

fn sort_descending(xs: &mut [i32]) {
    xs.sort_by(|a, b| b.cmp(a))
}

fn sort_by_length(words: &mut [String]) {
    words.sort_by(|a, b| a.len().cmp(&b.len()))
}

fn sort_pairs_by_second(pairs: &mut [(String, i32)]) {
    pairs.sort_by(|a, b| a.1.cmp(&b.1))
}

fn main() {
    let mut numbers = [3, 1, 4, 2];
    sort_descending(&mut numbers);
    println!("descending: {:?}", numbers);

    let mut words = vec![
        String::from("rust"),
        String::from("a"),
        String::from("slice"),
    ];
    sort_by_length(&mut words);
    println!("by length: {:?}", words);

    let mut pairs = vec![
        (String::from("a"), 3),
        (String::from("b"), 1),
        (String::from("c"), 2),
    ];
    sort_pairs_by_second(&mut pairs);
    println!("by second: {:?}", pairs);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sorts_numbers_descending() {
        let mut xs = [3, 1, 4, 2];
        sort_descending(&mut xs);
        assert_eq!(xs, [4, 3, 2, 1]);
    }

    #[test]
    fn sorts_strings_by_length() {
        let mut words = vec![
            String::from("rust"),
            String::from("a"),
            String::from("slice"),
        ];
        sort_by_length(&mut words);
        assert_eq!(words, vec!["a", "rust", "slice"]);
    }

    #[test]
    fn sorts_pairs_by_second_value() {
        let mut pairs = vec![
            (String::from("a"), 3),
            (String::from("b"), 1),
            (String::from("c"), 2),
        ];
        sort_pairs_by_second(&mut pairs);
        assert_eq!(
            pairs,
            vec![
                (String::from("b"), 1),
                (String::from("c"), 2),
                (String::from("a"), 3),
            ]
        );
    }
}
