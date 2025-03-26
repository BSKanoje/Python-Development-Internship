# Write a Python program to remove a key from a dictionary.

my_dict = {'a': 10, 'b': 20, 'c': 30}

key_to_remove = 'b'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]

print("Updated dictionary:", my_dict)
