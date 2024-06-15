from my_functions import math_functions as mf
# Explicit import
# from my_functions.math_functions import add_numbers, divide_numbers, multiply_numbers

# import all
# from my_functions.math_functions import *

result = mf.add_numbers(10, 20)
result = mf.divide_numbers(result, 20)
result = mf.multiply_numbers(result, 20)
print(result)
