// Exercise 3: Access array or slice elements safely with get().
//
// Run:
// rustc --edition=2021 --test 03_safe_get.rs && ./03_safe_get

fn get_value(xs: &[i32], index: usize) -> Option<i32> {
    xs.get(index).copied()
}

fn value_or_default(xs: &[i32], index: usize, default: i32) -> i32 {
    xs.get(index).copied().unwrap_or(default)
}

fn main() {
    let xs = [10, 20, 30];

    println!("{:?}", get_value(&xs, 1));
    println!("{:?}", get_value(&xs, 10));
    println!("{}", value_or_default(&xs, 10, -1));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_some_when_index_exists() {
        let xs = [10, 20, 30];
        assert_eq!(get_value(&xs, 1), Some(20));
    }

    #[test]
    fn returns_none_when_index_is_out_of_range() {
        let xs = [10, 20, 30];
        assert_eq!(get_value(&xs, 3), None);
    }

    #[test]
    fn returns_default_when_index_is_out_of_range() {
        let xs = [10, 20, 30];
        assert_eq!(value_or_default(&xs, 99, -1), -1);
    }
}
