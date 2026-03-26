# Nilikantha series in python

def pi(itera=1001):
    pi = 3
    sign = 1
    
    for i in range(2, itera, 2):
        pi += sign * (4/(i*(i+1)*(i+2))) # Add (+-) 4/i(i+1)(i+2)
        sign *= -1 # Alternate signs

    return pi

pi = pi()
print(chr(0x03c0)+' is approximately '+ str(round(pi,8)))
