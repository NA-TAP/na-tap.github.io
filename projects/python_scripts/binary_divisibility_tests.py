# ----------------------------------
# Binary Divisibility Test Functions
# ----------------------------------

def is_divisible_by_1(n):
    # Every number is divisible by 1
    return True

def is_divisible_by_2(n):
    # Check if the least significant bit is 0
    return (n & 1) == 0

def is_divisible_by_3(n):
    # Group bits in 2s (because 2^2 ≡ 1 mod 3) and sum them
    total = 0
    while n:
        total += n & 0b11  # Extract last 2 bits
        n >>= 2            # Shift right by 2 bits
    return total % 3 == 0

def is_divisible_by_4(n):
    # Check if the last two bits are 00
    return (n & 0b11) == 0

def is_divisible_by_5(n):
    # Group bits in 4s (because 2^4 ≡ 1 mod 5) and sum them
    total = 0
    while n:
        total += n & 0b1111  # Extract last 4 bits
        n >>= 4              # Shift right by 4 bits
    return total % 5 == 0

def is_divisible_by_6(n):
    # Must be divisible by both 2 and 3
    return is_divisible_by_2(n) and is_divisible_by_3(n // 2)

def is_divisible_by_7(n):
    # Group bits in 3s (because 2^3 ≡ 1 mod 7) and sum them
    total = 0
    while n:
        total += n & 0b111  # Extract last 3 bits
        n >>= 3             # Shift right by 3 bits
    return total % 7 == 0

def is_divisible_by_8(n):
    # Check if the last three bits are 000
    return (n & 0b111) == 0

def is_divisible_by_9(n):
    # Count number of 1s in binary representation
    # Similar to "sum of digits" rule in base-10
    return bin(n).count('1') % 9 == 0

def is_divisible_by_10(n):
    # Must be divisible by both 2 and 5
    return is_divisible_by_2(n) and is_divisible_by_5(n // 2)

# -------------------------
# Function to Run All Tests
# -------------------------

def run_divisibility_tests(binary_str):
    try:
        # Convert input string from binary to decimal
        n = int(binary_str, 2)
    except ValueError:
        print("Invalid binary number. Please enter a valid string of 0s and 1s.")
        return

    # Display the input and its decimal equivalent
    print(f"\nTesting binary: {binary_str}")
    print(f"Decimal value: {n}\n")

    # Run tests for numbers 1 through 10
    for i in range(1, 11):
        # Look up the corresponding function by name
        func = globals()[f'is_divisible_by_{i}']
        result = func(n)
        print(f"Divisible by {i}? {'Yes' if result else 'No'}")

# ----
# Main
# ----