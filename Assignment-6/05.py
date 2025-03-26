# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle

def check_triangle_type(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        if x == y == z:
            return "Equilateral triangle"
        elif x == y or y == z or x == z:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"
    else:
        return "Not a valid triangle"

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

triangle_type = check_triangle_type(x, y, z)

print(triangle_type)
