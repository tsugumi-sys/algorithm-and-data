// Exercise 5: Use Vec when the number of elements changes at runtime.
//
// Run:
// rustc --edition=2021 --test 05_vec_basics.rs && ./05_vec_basics

fn collect_even_numbers(xs: &[i32]) -> Vec<i32> {
    let mut vec = Vec::new();
    for n in xs {
        if n % 2 == 0 {
            vec.push(*n);
        }
    }
    vec
}

fn first_n_numbers(n: i32) -> Vec<i32> {
    let mut vec = Vec::new();
    for i in 1..n + 1 {
        vec.push(i);
    }
    vec
}

fn array_to_vec(xs: [i32; 4]) -> Vec<i32> {
    xs.to_vec()
}

fn main() {
    let xs = [1, 2, 3, 4, 5, 6];

    println!("evens: {:?}", collect_even_numbers(&xs));
    println!("first n: {:?}", first_n_numbers(5));
    println!("vec: {:?}", array_to_vec([10, 20, 30, 40]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn collects_even_numbers() {
        let xs = [1, 2, 3, 4, 5, 6];
        assert_eq!(collect_even_numbers(&xs), vec![2, 4, 6]);
    }

    #[test]
    fn builds_first_n_numbers() {
        assert_eq!(first_n_numbers(5), vec![1, 2, 3, 4, 5]);
    }

    #[test]
    fn non_positive_n_returns_empty_vec() {
        assert_eq!(first_n_numbers(0), Vec::<i32>::new());
        assert_eq!(first_n_numbers(-3), Vec::<i32>::new());
    }

    #[test]
    fn converts_array_to_vec() {
        assert_eq!(array_to_vec([10, 20, 30, 40]), vec![10, 20, 30, 40]);
    }
}
