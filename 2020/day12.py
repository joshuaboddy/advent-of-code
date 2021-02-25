import pandas as pd

with open('day12input.txt', 'r') as file:
    
    input = [line.strip() for line in file]
    
    facing = 90
    
    face_dict = dict([
                    (90, 'E'),
                    (180, 'S'),
                    (270,'W'),
                    (0, 'N')
                    ])
    
    coord = [0,0]
    
    def rules(coord, instruction, facing):
        
        go = line[0]
        val = int(line[1:])
        
        if go == 'F':
            go = face_dict[facing]
        if go == 'R':
            facing = (facing + val) % 360
        if go == 'L':
            facing = (facing - val) % 360
            
            
        if go == 'N':
            coord[1] += val
        if go == 'S':
            coord[1] += -val
        if go == 'E':
            coord[0] += val
        if go == 'W':
            coord[0] += -val
            
        return coord, facing
    
    for line in input:
        go = line[0]
        val = int(line[1:])
        
        coord, facing = rules(coord, line, facing)

