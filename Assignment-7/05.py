# Write a Python program to iterate over dictionaries using for loops.

my_dict = {'a': 10, 'b': 20, 'c': 30}

print("Iterating over keys:")
for key in my_dict:
    print(key)

print("Iterating over values:")
for value in my_dict.values():
    print(value)

print("Iterating over key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
