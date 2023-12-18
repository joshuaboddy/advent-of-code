import itertools
import re

f = open("test.txt", "r")

lines = f.readlines()
valid_combos = 0

for line in lines:
    line = line.strip().split(' ')
    springs = line[0] 
    seq = line[1]
    
    order_of_springs_needed = [int(x) for x in re.findall(r'-?\d+', seq)]
    number_of_springs_needed = sum(order_of_springs_needed)
    
    number_of_springs = springs.count('#')
    number_of_unknowns = springs.count('?')
    
    indices_of_unknowns = [idx for idx, char in enumerate(springs) if char == '?']
    
    combos = itertools.combinations(indices_of_unknowns, number_of_springs_needed - number_of_springs)
    
    for combo in combos:
        new_springs = springs
        for idx in combo:
            new_springs = new_springs[:idx] + '#' + new_springs[idx+1:]
        
        new_spring_seq = new_springs.replace('?','.').split('.')
        new_spring_seq_str = ','.join(str(len(hashes)) for hashes in new_spring_seq if hashes != '')
    
        if new_spring_seq_str == seq:
            valid_combos += 1
            
print(valid_combos)