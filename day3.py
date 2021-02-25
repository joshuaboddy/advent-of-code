import numpy as np

with open('C:/Users/jboddy/Desktop/aoc/2020/day3input.txt', 'r') as file:
    
    input = [line.strip() for line in file]
   
    parsed_data = list(enumerate(input))
    
    part_1 = sum([(int(line[enum * 3 % len(line)] == '#')) for (enum, line) in parsed_data])
    print(part_1)
    
    jumper_right = [1,3,5,7,1]
    jumper_down = [1,1,1,1,2]
    part_2 = 1
    for (jump_right, jump_down) in zip(jumper_right, jumper_down):
        part_2 = part_2 * sum([int(line[int(enum * jump_right / jump_down % len(line))] == '#') for (enum, line) in parsed_data if (enum % jump_down) == 0])
    print(part_2)
    