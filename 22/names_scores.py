#!/usr/bin/python3
#names_scores.py
import sys
import string
fname = sys.argv.pop()

def name_score(name):
    score = 0
    for letter in list(name):
        if (ord(letter)>=65 and ord(letter)<=90):
            score += (ord(letter) - 64)
    return score

total_score = 0
n_line = 1
with open(fname, "r") as f:
    for line in f:
        total_score += n_line * name_score(line.strip())
        n_line += 1
print("The total score is {}".format(total_score))

