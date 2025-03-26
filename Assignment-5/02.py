# Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict

# print(char_frequency('google.com'))

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    dict = max_to_min(dict)
    return dict

# the printed result must show frequency of each character in the string from maximum to minimum
def max_to_min(dict):
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return dict

print(char_frequency('google.com'))



