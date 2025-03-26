# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string

check_string = lambda s: any(x.isupper() for x in s) and any(x.islower() for x in s) and any(x.isdigit() for x in s) and len(s) >= 10
print(check_string("PaceWisd0m"))
