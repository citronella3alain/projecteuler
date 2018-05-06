fn main() {
	let mut total = 0;
	for i in 1..501{
		total += (16*(i))u32.pow(2) + 4*i + 4;
	}
	println!("{}", total);
}
