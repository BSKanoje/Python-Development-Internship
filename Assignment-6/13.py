# Take 10 integers from keyboard using loop and print their average value on the screen.

sum = 0
for i in range(10):
    sum += int(input(f"Enter number - {i+1}: "))
print("Average: ", sum/10)
