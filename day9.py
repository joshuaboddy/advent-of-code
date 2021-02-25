from itertools import combinations
import time 

start_time = time.time_ns()

with open('day9input.txt', 'r') as file:
    
    input = [int(line.strip()) for line in file]
    
    for i in range(len(input) - 25):
        exists = 0
        for combo in combinations(input[i:i+25],2):
            if sum(combo) == input[i+25]:
                exists += 1

        if exists == 0:
            value = input[i+25]
            index = i+25
            print(value)
            break
   
    for i in range(index):
        for j in range(index-i):
            if sum(input[i:i+j]) == value:
                print(max(input[i:i+j]) + min(input[i:i+j]))
                break
            
print(str(time.time_ns() - start_time) + ' nanoseconds')