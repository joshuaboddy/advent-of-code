import pandas as pd
import numpy as np

with open('2020/day13input.txt', 'r') as file:
    
    input = [line.strip() for line in file]
    
    part_1 = []
    
    for id in input[1].split(','):
        if id != 'x':
            diff = (int(int(input[0])/int(id)) + 1)*int(id) - int(input[0])
            if part_1 == [] or diff < part_1[1]:
                part_1 = [int(id), diff]
                
    print(np.prod(part_1))
          
    nums = []
    max_n = 1
    for enum, num in enumerate(input[1].split(',')):
        try:
            nums.append([enum, int(num)])
            max_n*=int(num)
        except:
            continue

    part_2 = sum([-offset * max_n/p * pow(int(max_n/p), p-2, p) for offset, p in nums]) % max_n

    print(part_2)
    

    
    
