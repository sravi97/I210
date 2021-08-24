from tools import *

# This file will test the functionality of your swap() function in tools.py

# DON'T ADD ANY NEW CODE TO THIS FILE!

# All new code goes in tools.py

# Here we test a single swap
letters = ["C", "B", "A", "D"]
swap(letters, 0, 2)
print("The list of letters should now be ['A', 'B', 'C', 'D']:", letters)

# Here we test several swaps
numbers = [4,1,2,3,5,6]
swap(numbers, 0, 1)
swap(numbers, 1, 2)
swap(numbers, 2, 3)
print("The list of numbers should now be [1, 2, 3, 4, 5, 6]:", numbers)
