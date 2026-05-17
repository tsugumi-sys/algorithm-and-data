// Exercise 2: Find the next greater element for each value.
//
// Run:
// rustc --edition=2021 --test 02_next_greater_element.rs && ./02_next_greater_element

#![allow(unused)]

fn next_greater_elements(nums: &[i32]) -> Vec<i32> {
    let mut stack = Vec::new();
    let mut ans = vec![-1; nums.len()];
    for i in 0..nums.len() {
        while let Some(&j) = stack.last() {
            if nums[j] < nums[i] {
                ans[j] = nums[i];
                stack.pop();
            } else {
                break;
            }
        }
        stack.push(i);
    }
    ans
}

fn main() {
    println!("{:?}", next_greater_elements(&[2, 1, 2, 4, 3]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn finds_next_greater_elements() {
        assert_eq!(
            next_greater_elements(&[2, 1, 2, 4, 3]),
            vec![4, 2, 4, -1, -1]
        );
    }

    #[test]
    fn returns_minus_one_when_not_found() {
        assert_eq!(next_greater_elements(&[5, 4, 3]), vec![-1, -1, -1]);
    }

    #[test]
    fn handles_empty_slice() {
        assert_eq!(next_greater_elements(&[]), Vec::<i32>::new());
    }
}
