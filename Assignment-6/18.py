# From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

div_by_3 = []
div_by_4 = []
div_by_5 = []
div_by_6 = []
div_by_7 = []
div_by_8 = []
div_by_9 = []
div_by_10 = []
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for num in even_numbers + odd_numbers:
    if num % 4 == 0:
        div_by_4.append(num)
    if num % 6 == 0:
        div_by_6.append(num)
    if num % 8 == 0:
        div_by_8.append(num)
    if num % 10 == 0:
        div_by_10.append(num)
    if num % 3 == 0:
        div_by_3.append(num)
    if num % 5 == 0:
        div_by_5.append(num)
    if num % 7 == 0:
        div_by_7.append(num)
    if num % 9 == 0:
        div_by_9.append(num)

print("Numbers divisible by 4:", div_by_4)
print("Numbers divisible by 6:", div_by_6)
print("Numbers divisible by 8:", div_by_8)
print("Numbers divisible by 10:", div_by_10)
print("Numbers divisible by 3:", div_by_3)
print("Numbers divisible by 5:", div_by_5)
print("Numbers divisible by 7:", div_by_7)
print("Numbers divisible by 9:", div_by_9)
