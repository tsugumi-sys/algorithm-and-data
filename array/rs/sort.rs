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

    let v = vec![5, 2, 8, 1, 9]; // stored in heap, dynamic sizing.
    println!("{:?}", v);
}
