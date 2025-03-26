# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

def swap_first_two_chars(str1, str2):
  return str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print(swap_first_two_chars(str1, str2))
