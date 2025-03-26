# Write a Python program to remove duplicates from Dictionary.

my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
unique_dict = {v: k for k, v in my_dict.items()}
unique_dict = {v: k for k, v in unique_dict.items()}

print("Dictionary after removing duplicates:", unique_dict)
