import numpy as np
from itertools import combinations
import time 

start_time = time.time()

with open('2020/day1input.txt', 'r') as file:
    input = [int(line.strip()) for line in file]
    
    for combo in combinations(input, 2):
        if sum(combo) == 2020:
            print(np.prod(combo))
            break
        
    for combo in combinations(input, 3):
        if sum(combo) == 2020:
            print(np.prod(combo))
            break

print(time.time() - start_time)