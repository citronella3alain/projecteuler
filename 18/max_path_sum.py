#!/bin/python3
# max_path_sum.py
import sys
f = open(sys.argv[1], "r")
fh = f.readlines()
tree = []
for line in fh:
	tree.append(list(map(int, line.rstrip().split())))
print(tree)

def path_sum(row, col):
	if row == len(tree) - 1:
		return tree[row][col]
	return tree[row][col] + max(path_sum(row+1,col), path_sum(row+1, col+1))

print(path_sum(0,0))
