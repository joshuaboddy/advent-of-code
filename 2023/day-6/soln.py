import re
import math

f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]


def parse_lines(lines, part1=True):
    time_strings = re.findall(r'\d+', lines[0])
    distance_strings = re.findall(r'\d+', lines[1])

    if part1:
        times = [int(x) for x in time_strings]
        distances = [int(x) for x in distance_strings]
    
    else:
        times = [int(''.join(time_strings))]
        distances = [int(''.join(distance_strings))]
        
    return times, distances
    

def quadratic_formula(a, b, c):
    sol1 = (-b-math.sqrt(b**2 - 4*a*c))/(2*a)
    sol2 = (-b+math.sqrt(b**2 - 4*a*c))/(2*a)
    
    return sol1, sol2


def product_of_wins(lines, part1=True):
    
    times, distances = parse_lines(lines, part1)
    
    product_of_wins = 1
    for time, distance in zip(times, distances):
        lowest, highest = quadratic_formula(1, -time, distance)
        product_of_wins *= (math.ceil(highest - 1) - math.floor(lowest))
        
    return product_of_wins


print(product_of_wins(lines, part1=True))
print(product_of_wins(lines, part1=False))
        