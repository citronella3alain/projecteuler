#!/usr/bin/python3
#double_base_palindromes.py
import sys

def is_double_base_palindrome(val):
    if (str(val)==str(val)[::-1] and str(bin(val)[2:]) == str(bin(val)[2:])[::-1]):
        return True
    return False


total = 0
for i in list(range(1000000)):
    if (is_double_base_palindrome(i)):
        total += i
print("The total is {}", total)
