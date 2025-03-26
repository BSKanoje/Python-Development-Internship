# Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

list1 = [{}, {}, {}]
list2 = [{1: 2}, {}, {}]

def are_all_dicts_empty(dict_list):
    return all(not d for d in dict_list)

print("Are all dictionaries in list1 empty?", are_all_dicts_empty(list1))
print("Are all dictionaries in list2 empty?", are_all_dicts_empty(list2))
