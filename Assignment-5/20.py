# Write a Python program to remove all consecutive duplicates of a given string.

from itertools import groupby

def remove_consecutive_duplicates(s):
    return ''.join(char for char, _ in groupby(s))

input_string = "aaabbbcccaaaaddd"
result = remove_consecutive_duplicates(input_string)

print(f"Original string: {input_string}")
print(f"String after removing consecutive duplicates: {result}")