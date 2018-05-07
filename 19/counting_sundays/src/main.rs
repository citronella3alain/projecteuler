pub struct Date {
	pub month: u64,
	pub day: u64,
	pub year: u64,
	pub day_of_week: u64, // Sunday = 0, Monday = 1 ... Saturday = 6
}
impl Date {
	pub fn next_day(&mut self) -> (){ //return day_of_week
		self.day_of_week = (self.day_of_week+1)%7;
		match self.month {
			1 | 3 | 5 | 7 | 8 | 10 => {
				//long month
				if self.day == 31{
					// month increases and day refreshes
					self.month += 1;
					self.day = 1
				}
				else {
					self.day += 1;
				}
			},
			2 => {
				//February
				if self.year % 4 == 0 && self.year % 400 != 0{
					// Tis a leap year
					if self.day == 29{
						self.day = 1;
						self.month += 1;
					}
					else {
						self.day += 1;
					}
				}
				else {
					// Tisnt a leap year
					if self.day == 28{
						self.month += 1;
						self.day = 1;
					}
					else {
						self.day += 1;
					}
				}	
			},
			4 | 6 | 9 | 11 => {
				//short month
				if self.day == 30{
					//month increases and day refreshes
					self.month += 1;
					self.day = 1;
				}
				else {
					self.day += 1;
				}
			},
			12 => {
				// December
				if self.day == 31{
					//year increases, day and month refresh
					self.year += 1;
					self.day = 1;
					self.month = 1;
				}
				else {
					self.day += 1;
				}
			},
			_ => println!("ERROR"),			
		}
	}
}
fn main() {
	let mut day = Date { month: 1, day: 1, year: 1901, day_of_week: 2};
	let mut count = 0;
//	println!("DATE \t Day of Week");
//	while day.month != 12 && day.day != 31 && day.year != 2000{
	loop{
		if day.month == 12 && day.day == 31 && day.year == 2000{
			break;
		}
		if day.day_of_week == 0 && day.day == 1{
			count+=1;
		}
		day.next_day();
		//println!("{} {} {} \t {}", day.month, day.day, day.year, day.day_of_week);
	}
	println!("{} Sundays fell on the first of the month during the twentieth century", count);
	
}
