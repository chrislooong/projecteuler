# Strategy: get next triangle number, find the number of factors by parsing the numbers until its square root`
import math

triangle_number = 1
triangle_incrementer = 1
while True:
    to_be_divided = triangle_number
    num_factors = 0
    potential_factor = 1
    while potential_factor <= math.sqrt(triangle_number):
        if triangle_number % potential_factor == 0:
            if math.sqrt(triangle_number) == potential_factor:
                num_factors += 1
            else:
                num_factors += 2
        potential_factor += 1
    if num_factors > 500:
        break
    triangle_incrementer += 1
    triangle_number += triangle_incrementer
print(triangle_number)
