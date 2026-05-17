// Exercise 4: Implement a FIFO queue with VecDeque.
//
// Run:
// rustc --edition=2021 --test 04_queue_with_vecdeque.rs && ./04_queue_with_vecdeque

#![allow(unused)]

use std::collections::VecDeque;

struct Queue {
    values: VecDeque<i32>,
}

impl Queue {
    fn new() -> Self {
        Self {
            values: VecDeque::new(),
        }
    }

    fn enqueue(&mut self, value: i32) {
        self.values.push_back(value);
    }

    fn dequeue(&mut self) -> Option<i32> {
        self.values.pop_front()
    }

    fn front(&self) -> Option<i32> {
        self.values.front().copied()
    }

    fn len(&self) -> usize {
        self.values.len()
    }
}

fn main() {
    let mut queue = Queue::new();
    queue.enqueue(10);
    println!("{:?}", queue.front());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn dequeues_in_fifo_order() {
        let mut queue = Queue::new();

        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        assert_eq!(queue.dequeue(), Some(10));
        assert_eq!(queue.dequeue(), Some(20));
        assert_eq!(queue.dequeue(), Some(30));
    }

    #[test]
    fn checks_front_without_removing() {
        let mut queue = Queue::new();

        queue.enqueue(10);
        queue.enqueue(20);

        assert_eq!(queue.front(), Some(10));
        assert_eq!(queue.len(), 2);
    }

    #[test]
    fn returns_none_when_empty() {
        let mut queue = Queue::new();

        assert_eq!(queue.front(), None);
        assert_eq!(queue.dequeue(), None);
        assert_eq!(queue.len(), 0);
    }
}
