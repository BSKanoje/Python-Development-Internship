# Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

n = int(input("Enter the number of elements in the list: "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

to_delete = input("Enter the element to delete: ")

if to_delete in user_list:
    user_list.remove(to_delete)
    print(f"'{to_delete}' has been deleted from the list.")
else:
    print(f"'{to_delete}' not found in the list.")

print("Updated list after deletion:")
for item in user_list:
    print(item)
