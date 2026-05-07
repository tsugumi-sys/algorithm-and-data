fn main() {
    let mut s1: String = String::from("hello"); // ヒープ（所有）
    let s2: &str = "hello"; // 文字列リテラル（参照）

    s1.push_str(" world"); // string, ""
    s1.push('!'); // char ''
    println!("{:?}", s1);
    let s3 = format!("{} {}", "hello", "world");
    println!("{:?}", s3);
    println!("{:?}", s3.contains("world"));
    println!("{:?}", s3.starts_with("world"));
    println!("{:?}", s3.ends_with("world"));

    if let Some(pos) = s3.find("world") {
        println!("{}", pos);
    }

    let s = "a,b,c"; // &str, embedded into the binary data.
    let vec: Vec<&str> = s.split(',').collect();
    println!("{:?}", vec);
    println!("{:?}", s3.replace("world", "Rust"));
    println!("{}", s3.len());
    for c in s3.chars() {
        println!("{}", c);
    }
    println!("{:?}", s3.chars().nth(5));
}
