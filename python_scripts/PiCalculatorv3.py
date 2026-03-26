pi = 0
neg = 1
for i in range(1,1000000,2):
    pi += neg * (4/i)
    neg *= -1
print(pi)

