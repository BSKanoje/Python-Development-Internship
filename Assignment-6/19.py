# From a list containing ints, strings and floats, make three lists to store them separately.

mixed_list = [10, 'apple', 3.14, 25, 'banana', 7.5, 42, 'orange', 100, 2.718]
int_list = []
str_list = []
float_list = []

for item in mixed_list:
    if isinstance(item, int):
        int_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)

print("Integer List:", int_list)
print("Float List:", float_list)
print("String List:", str_list)
