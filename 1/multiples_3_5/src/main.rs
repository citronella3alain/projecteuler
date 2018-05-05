fn main() {
	let mut total = 0;
	for x in 0..1001{
		if x % 3 == 0{
			total += x;
		}
		else if x % 5 == 0{
			total += x;
		}
	}
	println!("The total is {}", total);
}
