import itertools
import math

# Function to check if three points form a right isosceles triangle
def is_right_isosceles(p1, p2, p3):
    distances = [
        math.dist(p1, p2),
        math.dist(p2, p3),
        math.dist(p3, p1)
    ]
    distances.sort()
    # Check if two sides are equal and the square of the hypotenuse is the sum of the squares of the other two sides
    return math.isclose(distances[0], distances[1]) and math.isclose(distances[2]**2, distances[0]**2 + distances[1]**2)

# Coordinates of the 13 coins in 5-4-5-4-5 arrangement with half offset
coins = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0.5, 1), (1.5, 1), (2.5, 1), (3.5, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0.5, 3), (1.5, 3), (2.5, 3), (3.5, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]

# Count the number of right isosceles triangles
triangle_count = 0
for combination in itertools.combinations(coins, 3):
    if is_right_isosceles(*combination):
        triangle_count += 1

print(f"Number of right isosceles triangles: {triangle_count}")

# Print the arrangement of coins in a more intuitive format
print("Coin Arrangement:")
for y in range(5):
    if y % 2 == 0:
        print("O O O O O")
    else:
        print(" O O O O")
