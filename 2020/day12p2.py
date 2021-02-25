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
    
    waypoint = [10,1]
    
    me = [0,0]
    
    def rules(waypoint, instruction, facing, me):
        
        go = line[0]
        val = int(line[1:])
        
        if go == 'F':
            me = [me[0] + waypoint[0]*val, me[1] + waypoint[1]*val] 
        if go == 'R':
            if val == 270:
                waypoint = [-waypoint[1], waypoint[0]]
            if val == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            if val == 90:
                waypoint = [waypoint[1], -waypoint[0]]
        if go == 'L':
            if val == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            if val == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            if val == 270:
                waypoint = [waypoint[1], -waypoint[0]]
            
            
        if go == 'N':
            waypoint[1] += val
        if go == 'S':
            waypoint[1] += -val
        if go == 'E':
            waypoint[0] += val
        if go == 'W':
            waypoint[0] += -val
            
        return waypoint, facing, me
    
    for line in input:
        go = line[0]
        val = int(line[1:])
        
        waypoint, facing, me = rules(waypoint, line, facing, me)

        
print(abs(me[0]) +abs(me[1]))