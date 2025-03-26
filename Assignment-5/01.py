# Write a Python program to calculate the length of a string.

def string_length(str1):
    # also counts blank spaces
    count = 0
    for char in str1:
        count += 1
    return count

print(string_length('HelloWorld!'))
print(string_length('Python Programming'))
print(string_length('Data Science'))
print(string_length('Machine Learning'))
print(string_length('Deep Learning'))