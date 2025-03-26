# Write a Python program that counts the number of elements within a list that are greater than 30.

def count_greater_than_30(lst):
    return sum(1 for num in lst if num > 30)

numbers = [10, 25, 35, 40, 29, 50, 60, 15, 31]
result = count_greater_than_30(numbers)
print("Count of numbers greater than 30:", result)
