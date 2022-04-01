from handy_functions.calc_functions import calc_pythagoras
import sys


name = sys.argv[1]
print(f"Hello {name}!")

print("Calculate your triangle")

a = sys.argv[2]
b = sys.argv[3]

a_float = float(a)
b_float = float(b)

c = calc_pythagoras(a_float, b_float)

print(f"The result is {c}")