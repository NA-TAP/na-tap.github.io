import math

def trig(theta):
    # Reduce theta to [0, 2π) for periodicity
    theta = theta % (2 * math.pi)
    
    # Initialize values for CORDIC rotation mode
    x = 1.0
    y = 0.0
    phi = theta
    n = 0
    change = 1
    maxiter = 100
    while n < maxiter and change > 0:
        if phi == 0:
            break  # Avoid division by zero
        d = phi / abs(phi)  # Sign of phi
        next_x = x - (d * y * math.pow(2, -n))
        next_y = y + (d * x * math.pow(2, -n))
        change = abs(next_x - x) + abs(next_y - y)
        next_phi = phi - (d * math.atan(math.pow(2, -n)))
        x = next_x
        y = next_y
        phi = next_phi
        n += 1

    # Return cos, sin, tan (handle tan when x == 0)
    if x == 0:
        tan_val = float('inf') if y > 0 else float('-inf')
    else:
        tan_val = y / x
    return (x, y, tan_val)

def sin(theta):
    cos, sin, tan = trig(theta)
    return sin

def cos(theta):
    cos, sin, tan = trig(theta)
    return cos

def tan(theta):
    cos, sin, tan = trig(theta)
    return tan
