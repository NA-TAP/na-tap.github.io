
def calculatePI(PI,n,sign):

	for i in range(0,1000000):
		PI = PI + (sign * (4 / ((n) * (n + 1)* (n + 2))))
		sign = sign * (-1)
		n += 2
	return PI

PI = 3
n = 2
sign = 1
a = calculatePI(PI, n, sign)
print("Pi is ",end="")
print(round(a,8))

