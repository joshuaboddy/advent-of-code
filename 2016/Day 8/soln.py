import numpy as np
from collections import deque

f = open('input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

grid = {}
for i in range(50):
    for j in range(6):
        grid[(i,j)] = '.'

for line in lines:
    if line[0:4] == 'rect':
        rows_and_columns = [int(x) for x in line[5:].strip().split('x')]
        for i, j in np.ndindex(tuple(rows_and_columns)):
            grid[(i,j)] = '#'
    elif 'row' in line:
        rotate_row = line.replace(' by ', '=').strip().split('=')
        rotate_row = [int(x) for x in rotate_row[1:3]]
        
        current_row = deque()
        for key in grid.keys():
            if rotate_row[0] == key[1]:
                current_row.append(grid[key])
        current_row.rotate(rotate_row[1])
        
        for key in grid.keys():
            if rotate_row[0] == key[1]:
                grid[key] = current_row[key[0]]
    elif 'column' in line:
        rotate_col = line.replace(' by ', '=').strip().split('=')
        rotate_col = [int(x) for x in rotate_col[1:3]]
        
        current_col = deque()
        for key in grid.keys():
            if rotate_col[0] == key[0]:
                current_col.append(grid[key])
        current_col.rotate(rotate_col[1])
        
        for key in grid.keys():
            if rotate_col[0] == key[0]:
                grid[key] = current_col[key[1]]
                
cnt = 0
for val in grid.values():
    if val == '#':
        cnt += 1
print(cnt)

for i in range(6):
    row = []
    for key in grid.keys():
        if i == key[1]:
            row.extend(grid[key])
    print(row)
