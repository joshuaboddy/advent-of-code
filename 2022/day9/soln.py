import numpy as np

raw = open('input.txt').readlines()

vectors = {"U": (0, 1),
           "D": (0, -1),
           "L": (-1, 0),
           "R": (1, 0)}


part = 2
rope_length = 10 if part == 2 else 2
rope = {i: (0,0) for i in range(rope_length)}
tail_position_set = {(0,0)}


for line in raw:
    line = line.strip().split()
    direction = line[0]
    amount = int(line[1])
    vector = vectors[direction]
    
    for i in range(1, amount + 1):
        head = rope[0]
        head = (head[0] + vector[0], head[1] + vector[1])  
        rope[0] = head
        
        for j in range(1, rope_length):
            prev = rope[j-1]
            current = rope[j]
        
            x_distance = prev[0] - current[0]
            y_distance = prev[1] - current[1]
            
            if abs(x_distance) >= 1 and abs(y_distance) >= 1 and (abs(x_distance) * abs(y_distance) != 1):
                current = (current[0] + np.sign(x_distance), current[1] + np.sign(y_distance))
            
            elif abs(x_distance) > 1:
                current = (current[0] + np.sign(x_distance), current[1])
                
            elif abs(y_distance) > 1:
                current = (current[0], current[1] + np.sign(y_distance))
                
            rope[j] = current
            
        tail_position_set = tail_position_set.union({rope[rope_length-1]})
        
print(len(tail_position_set))