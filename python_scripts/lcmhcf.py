def hcf(a,b):
    factors = []
    list = [a,b]
    list.sort()
    a=list[1]
    b=list[0]
    for i in range (1,a+1):
        if a%i == 0:
            factors.append(i)
    factors.reverse()
    for i in factors:
        if b%i==0:
            return i 
            break
def lcm(a,b):
    return a*b//hcf(a,b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
mode = str(input('hcf or lcm: '))
if mode == 'hcf':
    print(hcf(a,b))
elif mode == 'lcm':
    print(lcm(a,b))