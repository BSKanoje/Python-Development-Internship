# Write a Python program to print the index of the character in a string.

def print_character_indices(s):
    for index, char in enumerate(s):
        print(f"Character '{char}' is at index {index}")

input_string = "hello world"
print_character_indices(input_string)
