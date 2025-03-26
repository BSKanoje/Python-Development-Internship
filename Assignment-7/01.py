# Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 3, 'b': 1, 'c': 2}

sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_asc)

sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_desc)
