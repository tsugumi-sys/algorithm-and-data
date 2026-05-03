fn main() {
    let mut array: [i32; 3] = [0; 3]; // stored into the stack.

    array[0] = 1;
    array[1] = 3;
    array[2] = 2;

    println!("{:?}", array);
    array.sort();
    println!("sorted: {:?}", array);
    // {} → normal display（Displayトレイト）
    // {:?} → debug display（Debugトレイト）

    let mut v = vec![5, 2, 8, 1, 9]; // stored in heap, dynamic sizing.
    println!("{:?}", v);

    let mut left = 0;
    let mut right = v.len() - 1;
    while left < right {
        v.swap(left, right);
        left += 1;
        right -= 1;
    }
    println!("swapped: {:?}", v);

    v.reverse();
    println!("reversed: {:?}", v);
}
