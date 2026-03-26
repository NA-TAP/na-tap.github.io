# Me trying to do hex and bin and oct
def into_hex(num=20):
    if num == 0:
        return "0x0"
    digits = []
    digit = num & 0b1111
    while num > 0:
        if digit < 10:
            digits.append(str(digit))
        else:
            digits.append(str(chr(digit-10+65)))
        num //= 0b10000
        digit = num & 0b1111
    return '0x'+ "".join(reversed(digits))

def into_bin(num=20):
    if num == 0:
        return "0b0"
    digits = []
    digit = num & 0b1
    while num > 0:
        digits.append(str(digit))
        num //= 0b10
        digit = num & 0b1
    return '0b'+ "".join(reversed(digits))

def into_oct(num=20):
    if num == 0:
        return "0o0"
    digits = []
    digit = num & 0b111
    while num > 0:
        digits.append(str(digit))
        num //= 0b1000
        digit = num & 0b111
    return '0o'+ "".join(reversed(digits))


