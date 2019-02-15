#!/usr/bin/python3
# permutations.py

import sys
digits = list(range(10))
#digits = [1, 2, 3]
count = 0

def permutations(arr, unused):
#	print(arr)
#	print(unused)
	global count
	if len(unused) == 1:
		arr.extend(unused)
		count += 1
#		print(arr)
		if (count == 1000000):
			print(arr)
			sys.exit()
		return
	for i in list(range(len(unused))):
		arr.append(unused.pop(i))
		permutations(arr[:], unused[:])
		unused.insert(i, arr.pop())
permutations([], digits)
