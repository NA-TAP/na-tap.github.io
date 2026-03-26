#fraction adder

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(n1, d1, n2, d2):
    newn = n1*d2 + n2*d1
    newd = d1*d2
    g_c_d = gcd(newn, newd)
    newnewn = newn//g_c_d
    newnewd = newd//g_c_d
    return (newnewn, newnewd)
