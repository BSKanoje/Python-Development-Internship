# Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_list = []
for sublist in sample_list:
    if sublist not in unique_list:
        unique_list.append(sublist)

print("New List:", unique_list)
