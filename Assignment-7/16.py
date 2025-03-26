# Write a Python program to find the highest 3 values in a dictionary.

my_dict = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}
highest_values = sorted(my_dict.values(), reverse=True)[:3]

print("Highest 3 values:", highest_values)
