from handy_functions.calc_functions import calc_pythagoras


name = input("What is your name ?(Unkown)\n") or "Unkown"
print(f"Hello {name}!")

print("Calculate your triangle")

a = input("Insert the value for a\n") or 1
b = input("Insert the value for b\n") or 1

a_float = float(a)
b_float = float(b)

c = calc_pythagoras(a_float, b_float)

print(f"The result is {c}")