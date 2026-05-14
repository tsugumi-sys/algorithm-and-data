// Exercise 2: Practice iter(), iter_mut(), and into_iter().
//
// Run:
// rustc --edition=2021 --test 02_iter_variants.rs && ./02_iter_variants

fn sum_with_iter(xs: &[i32]) -> i32 {
    xs.iter().sum()
}

fn double_in_place(xs: &mut [i32]) {
    // todo!("Use iter_mut() to double every element")
    for el in xs.iter_mut() {
        *el *= 2;
    }
}

fn strings_into_vec(xs: [String; 3]) -> Vec<String> {
    todo!("Use into_iter() to move Strings into a Vec<String>")
}

fn main() {
    let mut numbers = [1, 2, 3];
    println!("sum: {}", sum_with_iter(&numbers));

    double_in_place(&mut numbers);
    println!("doubled: {:?}", numbers);

    let words = [
        String::from("rust"),
        String::from("array"),
        String::from("slice"),
    ];
    println!("words: {:?}", strings_into_vec(words));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sums_using_iter() {
        let xs = [2, 4, 6];
        assert_eq!(sum_with_iter(&xs), 12);
    }

    #[test]
    fn doubles_using_iter_mut() {
        let mut xs = [1, 3, 5];
        double_in_place(&mut xs);
        assert_eq!(xs, [2, 6, 10]);
    }

    #[test]
    fn moves_strings_into_vector() {
        let xs = [String::from("a"), String::from("b"), String::from("c")];
        assert_eq!(strings_into_vec(xs), vec!["a", "b", "c"]);
    }
}
