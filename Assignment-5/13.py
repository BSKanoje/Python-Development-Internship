# Write a Python program to check whether a string starts with specified characters.

def starts_with_specified_chars(s, specified_chars):
    return s.startswith(specified_chars)

input_string = "Hello, World!"
specified_characters = "Hello"

if starts_with_specified_chars(input_string, specified_characters):
    print(f"The string starts with '{specified_characters}'.")
else:
    print(f"The string does not start with '{specified_characters}'.")
