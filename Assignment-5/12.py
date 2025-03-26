# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_to_uppercase_if_condition_met(s):
    first_four = s[:4]
    uppercase_count = sum(1 for char in first_four if char.isupper())
    if uppercase_count >= 2:
        return s.upper()
    else:
        return s

input_string1 = "HeLLo World"
result1 = convert_to_uppercase_if_condition_met(input_string1)
print(result1)

input_string2 = "Hello World"
result2 = convert_to_uppercase_if_condition_met(input_string2)
print(result2)

input_string3 = "PYthon"
result3 = convert_to_uppercase_if_condition_met(input_string3)
print(result3)
