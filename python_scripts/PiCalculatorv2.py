from fractions import Fraction

# Compute pi using the Leibniz series with Fraction to avoid floating point
# arithmetic: pi = 4 * sum_{k=0..n-1} (-1)^k / (2k+1)

def pi_leibniz_fraction(terms=200):
    if terms < 1:
        raise ValueError('terms must be >= 1')
    total = Fraction(0, 1)
    sign = 1
    for k in range(terms):
        denom = 2 * k + 1
        total += Fraction(sign, denom)
        sign = -sign
    return Fraction(4, 1) * total


if __name__ == '__main__':
    TERMS = 2000  # increase for better approximation (beware of large rationals)
    pi_frac = pi_leibniz_fraction(TERMS)
    print('pi as Fraction:', pi_frac)
    # print a decimal approximation (float) for readability
    print('approx (float):', float(pi_frac))

