# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'

def not_poor(str):
    snot = str.find('not')
    spoor = str.find('poor')
    
    if spoor > snot and snot > 0 and spoor > 0:
        str = str.replace(str[snot:(spoor+4)], 'good')
        return str
    else:
        return str
    
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is not poor!'))
print(not_poor('The lyrics is poor!'))
