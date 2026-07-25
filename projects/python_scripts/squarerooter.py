def find_closest(numbers, target):
  if not numbers:
    return None

  closest = numbers[0]  # Initialize closest to the first number
  min_difference = abs(numbers[0] - target) # initialize min difference

  for number in numbers:
    difference = abs(number - target)
    if difference < min_difference:
      min_difference = difference
      closest = number

  return closest

def get_square_numbers(n=20):
  return [i ** 2 for i in range(1, n+1)]

def babilonian_sqrt(n, terms=100):
    if n < 0:
        raise ValueError('Cannot compute square root of negative numbers')
    
    if n == 0:
        return 0
    
    # Initial approximation
    approx = n / 2
    
    for i in range(terms):
        approx = (approx + (n / approx)) / 2  # Babylonian formula
    
    return approx

# Input handling
num = input('Enter a number: ')
terms = input('Enter the number of terms: ')

try:
    num = float(num)
    if not terms:
        print(babilonian_sqrt(num))
    else:
        print(babilonian_sqrt(num, int(terms)))
except ValueError as e:
    print(f"Error: {e}")


