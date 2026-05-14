// Exercise 4: Use windows() and chunks().
//
// Run:
// rustc --edition=2021 --test 04_windows_chunks.rs && ./04_windows_chunks

fn adjacent_differences(xs: &[i32]) -> Vec<i32> {
    let mut vec = Vec::new();
    for window in xs.windows(2) {
        vec.push(window[1] - window[0]);
    }
    vec
}

fn chunk_sums(xs: &[i32], chunk_size: usize) -> Vec<i32> {
    let mut vec = Vec::new();
    for chunk in xs.chunks(chunk_size) {
        vec.push(chunk.into_iter().sum());
    }
    vec
}

fn main() {
    let xs = [1, 4, 9, 16, 25];

    println!("diffs: {:?}", adjacent_differences(&xs));
    println!("chunk sums: {:?}", chunk_sums(&xs, 2));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_adjacent_differences() {
        let xs = [1, 4, 9, 16];
        assert_eq!(adjacent_differences(&xs), vec![3, 5, 7]);
    }

    #[test]
    fn short_slice_has_no_adjacent_differences() {
        let xs = [1];
        assert_eq!(adjacent_differences(&xs), Vec::<i32>::new());
    }

    #[test]
    fn returns_chunk_sums() {
        let xs = [1, 2, 3, 4, 5];
        assert_eq!(chunk_sums(&xs, 2), vec![3, 7, 5]);
    }
}
