# Write a Python program to convert a string in a list.

def string_to_list(s):
    return list(s)

input_string = "hello"

result = string_to_list(input_string)

print(f"String: {input_string}")

print(f"List: {result}")

# --------------

def string_to_list_with_delimiter(s, delimiter):
    return s.split(delimiter)

input_string = "apple,banana,cherry"

delimiter = ","

result = string_to_list_with_delimiter(input_string, delimiter)

print(f"String: {input_string}")

print(f"List with delimiter '{delimiter}': {result}")
