// Exercise 1: Use slices as function arguments.
//
// Run:
// rustc --edition=2021 --test 01_slice_args.rs && ./01_slice_args

// Learned:
// - sum() is an Iterator method, so we need to call iter() first.
// - xs is &[i32], which is a borrowed slice, not an iterator itself.
// - iter() borrows each element and yields &i32.
// - into_iter() can also work here because xs is already a reference.
// - In this case, iter() is clearer because we only need to read the slice.
fn sum_slice(xs: &[i32]) -> i32 {
    xs.iter().sum()
}

fn main() {
    let array = [1, 2, 3, 4];
    let vector = vec![5, 6, 7];

    println!("array sum: {}", sum_slice(&array));
    println!("vector sum: {}", sum_slice(&vector));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sums_an_array() {
        let xs = [1, 2, 3, 4];
        assert_eq!(sum_slice(&xs), 10);
    }

    #[test]
    fn sums_a_vector() {
        let xs = vec![5, 6, 7];
        assert_eq!(sum_slice(&xs), 18);
    }

    #[test]
    fn empty_slice_is_zero() {
        let xs: [i32; 0] = [];
        assert_eq!(sum_slice(&xs), 0);
    }
}
