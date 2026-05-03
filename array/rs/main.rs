fn main() {
    // To compile and run Rust code with rustc, you need to define a `main` function. It cannot be omitted.
    let mut array: [i32; 3] = [0; 3];

    array[1] = 1;
    array[2] = 2;

    assert_eq!([1, 2], &array[1..]);

    // This loop prints: 0 1 2
    for x in array {
        print!("{x} ");
    }

    println!("{:?}", array); // The item in the `array` uses Copy trait, so no error happens.

    let array = [String::from("a"), String::from("b")];
    for x in array {
        print!("{x} ")
    }

    // println!("{}", array); // The String data type is not use Copy trait, so compiler error happens.

    print!("{}", add(3, 4));
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}
