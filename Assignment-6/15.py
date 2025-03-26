# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

sum = 0
product = 1
count = 0
print("Enter 'q' to quit")
while True:
    n = input("Enter a number: ")
    if n == 'q':
        break
    else:
        n = int(n)
        sum += n
        product *= n
        count += 1
print("Average: ", sum/count)
print("Product: ", product)
