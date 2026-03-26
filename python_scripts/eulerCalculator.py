from math import factorial
n = 1
fact = 1
for i in range(1,10000):
    fact = fact*i
    n += 1/fact
print(n)