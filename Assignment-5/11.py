# Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_if_multiple_of_four(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s

input_string = "abcdefgh"
result = reverse_if_multiple_of_four(input_string)
print(result)

input_string2 = "abc"
result2 = reverse_if_multiple_of_four(input_string2)
print(result2)
