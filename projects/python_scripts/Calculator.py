# CALCULATOR
import math
print("operator (+ - * / square root cube root ^2 ^3 ^ nth root)")  # operator
operator = str(input())
print("number1")  # number 1
number1 = float(input())
print("number2 (does not matter if operator has only one number)")  # number 2
number2 = float(input())

print("Answer = ", end="")  # prints answer
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "square root":
    print(math.sqrt(number1))
elif operator == "cube root":
    print(math.cbrt(number1))
elif operator == "^2":
    print(number1 ** 2)
elif operator == "^3":
    print(number1 ** 3)
elif operator == "^":
    print(number1 ** number2)
elif operator == "nth root":
    print(number1 ** (1 / number2))

# yay! we're done.
