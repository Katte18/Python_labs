# Lab. work 2-2 (numbers)

import random
import math

# Generate sequence 5 integers long from range(0, 100)
sequence = random.sample(range(100), 5)
print('5 integers long from range(0, 100): {}'.format(sequence))

# Generate random float and print variables above
float = random.random()
print('random float: {}'.format(float))

# Find max element from generated sequence
max_int = max(sequence)
print(max_int)

# Find min element from generated sequence
min_int = min(sequence)
print(min_int)

# Make a floor division between max element and generated float
division = max_int // float
print(division)

# Find factorial of the result above
math.factorial(sequence) #error for processing line 27, in <module> math.factorial(sequence)
# TypeError: an integer is required (got type list)
math.factorial(float)
math.factorial(max_int)
math.factorial(division)
