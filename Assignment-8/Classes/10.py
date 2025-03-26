# Write a Python program to get the class name of an instance in Python.

class MyClass:
    pass

instance = MyClass()
print(instance.__class__.__name__)
