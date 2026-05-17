// Exercise 5: Return nodes in BFS order from a start node.
//
// Run:
// rustc --edition=2021 --test 05_simple_bfs.rs && ./05_simple_bfs

#![allow(unused)]

use std::collections::VecDeque;

fn bfs_order(graph: &[Vec<usize>], start: usize) -> Vec<usize> {
    let mut ans = Vec::new();
    if start > graph.len() - 1 {
        return ans;
    }
    ans.push(start);

    let mut queue = VecDeque::new();
    let mut visited = vec![false; graph.len()];

    queue.push_back(start);
    visited[start] = true;
    while let Some(node) = queue.pop_front() {
        for &e in &graph[node] {
            if !visited[e] {
                visited[e] = true;
                ans.push(e);
                queue.push_back(e);
            }
        }
    }
    ans
}

fn main() {
    let graph = vec![vec![1, 2], vec![3], vec![3], vec![]];
    println!("{:?}", bfs_order(&graph, 0));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn visits_nodes_in_bfs_order() {
        let graph = vec![vec![1, 2], vec![3], vec![3], vec![]];

        assert_eq!(bfs_order(&graph, 0), vec![0, 1, 2, 3]);
    }

    #[test]
    fn does_not_visit_disconnected_nodes() {
        let graph = vec![vec![1], vec![], vec![3], vec![]];

        assert_eq!(bfs_order(&graph, 0), vec![0, 1]);
    }

    #[test]
    fn returns_empty_vec_when_start_is_out_of_bounds() {
        let graph = vec![vec![1], vec![]];

        assert_eq!(bfs_order(&graph, 10), Vec::<usize>::new());
    }
}
