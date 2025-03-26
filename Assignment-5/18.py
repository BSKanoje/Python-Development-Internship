# Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23

def swap_comma_and_dot(s):
    translation_table = str.maketrans({',': '.', '.': ','})
    
    return s.translate(translation_table)

sample_string = "32.054,23"
result = swap_comma_and_dot(sample_string)

print(f"Original string: {sample_string}")
print(f"Swapped string: {result}")
