f = open('input.txt')
raw = f.readlines()
f.close()

part1grid = {}

lines = list(raw)
for y_coord, line in enumerate(lines):
    x_values = [int(num) for num in line.strip()]
    for x_coord, x in enumerate(x_values):
        part1grid[(x_coord, y_coord)] = x

part2grid = part1grid.copy()

def run_steps(grid):
    
    keys = list(grid.keys())
    keynums = len(keys)
    
    loop_me = True
    touched = []

    while loop_me:
        key_iterator=0
        while key_iterator < keynums:    
            key = keys[key_iterator]
            if key not in touched:
                if grid[key] > 9:
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if (i != 0) | (j != 0):
                                position = (key[0] + i, key[1] + j)
                                if position in grid:
                                    grid[position] = grid[position] + 1
                    touched = touched + [key]
                    key_iterator = 0
                else:
                    key_iterator += 1
            else: 
                key_iterator += 1
        loop_me = any([v for v in grid.values()]) == 10

    for key in grid:
        if grid[key] > 9:
            grid[key] = 0
            
    flashes = sum([1 for x in grid.values() if x == 0])
    
    return flashes, grid
            
#part 1
total_flashes = 0

for _ in range(100):
    
    #add 1 to each octopous
    for key, value in part1grid.items():
        part1grid[key] = part1grid[key] + 1 
        
    #run steps
    flashes, part1grid = run_steps(part1grid)  
    
    total_flashes += flashes   

print(total_flashes)

#part 2
step_number = 0

while sum(part2grid.values()) > 0:
    
    #add 1 to each octopous
    for key, value in part2grid.items():
        part2grid[key] = part2grid[key] + 1 
        
    #run steps
    flashes, part2grid = run_steps(part2grid)  
    
    step_number += 1

print(step_number)
