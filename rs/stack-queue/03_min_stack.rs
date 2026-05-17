// Exercise 3: Implement a stack that can return the current minimum in O(1).
//
// Run:
// rustc --edition=2021 --test 03_min_stack.rs && ./03_min_stack

#![allow(unused)]

struct MinStack {
    values: Vec<i32>,
    mins: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        Self {
            values: Vec::new(),
            mins: Vec::new(),
        }
    }

    fn push(&mut self, value: i32) {
        self.values.push(value);
        let min = match self.mins.last() {
            Some(&current_min) => current_min.min(value),
            None => value,
        };
        self.mins.push(min);
    }

    fn pop(&mut self) -> Option<i32> {
        self.mins.pop();
        self.values.pop()
    }

    fn top(&self) -> Option<i32> {
        self.values.last().copied()
    }

    fn get_min(&self) -> Option<i32> {
        self.mins.last().copied()
    }
}

fn main() {
    let mut stack = MinStack::new();
    stack.push(3);
    stack.push(1);
    println!("{:?}", stack.get_min());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tracks_minimum() {
        let mut stack = MinStack::new();

        stack.push(3);
        stack.push(1);
        stack.push(2);

        assert_eq!(stack.top(), Some(2));
        assert_eq!(stack.get_min(), Some(1));
    }

    #[test]
    fn restores_previous_minimum_after_pop() {
        let mut stack = MinStack::new();

        stack.push(3);
        stack.push(1);
        stack.push(2);

        assert_eq!(stack.pop(), Some(2));
        assert_eq!(stack.get_min(), Some(1));
        assert_eq!(stack.pop(), Some(1));
        assert_eq!(stack.get_min(), Some(3));
    }

    #[test]
    fn returns_none_when_empty() {
        let mut stack = MinStack::new();

        assert_eq!(stack.top(), None);
        assert_eq!(stack.get_min(), None);
        assert_eq!(stack.pop(), None);
    }
}
