#!/usr/bin/python3
# coded_triangle_numbers.py

import sys
import math
f = open(sys.argv[1], "r")
fh = f.readlines()
count = 0
for line in fh:
	val = 0
	for c in list(line.strip()):
		val += (ord(c) - ord('A') + 1)
	n = (math.sqrt(8*val + 1) - 1) / 2
	if (int(n) == n):
		count += 1
		print ("{}: \t value:{} \t n : {}".format(line.strip(), val, n))
print ("The count is {}".format(count))
