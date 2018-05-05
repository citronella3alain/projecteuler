#!/usr/bin/python3
#number_letter_counts.py
import sys

one_through_nineteen = ["",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"]

tens = ["",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"]

#for i in list(range(len(tens))):
#	print("{}: {}".format(i, tens[i]))


def word_representation(val):
	if val == 1000:
		return "one thousand", len("onethousand")
	word_number = ""
	char_count = 0
	hundreds = int(val / 100)
	val %= 100
	if (hundreds != 0):
		word_number += (one_through_nineteen[hundreds] + " hundred ")
		char_count += (len(one_through_nineteen[hundreds])+7)
	if val == 0:
		return word_number, char_count
	if (hundreds != 0):
		word_number += "and "
		char_count += 3
	if (val > 19):
		ones = val % 10
		word_number += (tens[int(val/10)] + " ")
		char_count += len(tens[int(val/10)])
		word_number += one_through_nineteen[ones]
		char_count += len(one_through_nineteen[ones])
	else:
		word_number += one_through_nineteen[val]
		char_count += len(one_through_nineteen[val])
	return word_number, char_count

print(word_representation(int(sys.argv[1])))
total = 0
print("# \t Word Representation \t Length excluding spaces \t Cumulative Length")
for i in list(range(1, 1001)):
	word_number, length = word_representation(i)
	total += length 
	print("{} \t {} \t {} \t {}".format(i, word_number, length, total))
