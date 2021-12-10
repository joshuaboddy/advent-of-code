f = open('day24input.txt')
raw = f.readlines()
f.close()

d = {}

lines = list(raw)

moves = {'e': (2,0),
         'w': (-2,0),
         'ne': (1,1),
         'nw': (-1,1),
         'se': (1,-1),
         'sw': (-1,-1)}

def make_move(tile, move, directions):
    
    d = directions[move]
    
    return (tile[0] + d[0], tile[1] + d[1])

#part 1

tile = (0,0)

h = {}
h[tile] = 0
current_tile = tile

for line in lines:
    
    inst = []
    
    line = line.strip()
    
    i = 0
   
    while i < len(line):
        
        if line[i:i+2] in ['se', 'sw', 'ne', 'nw']:
            inst.append(line[i:i+2])
            i = i+2
            
        else:
            inst.extend(line[i])
            i = i+1

    for move_num, move in enumerate(inst):
        
        next_tile = make_move(current_tile, move, moves)    
        
        if move_num != (len(inst)-1):
            h[next_tile] = h.get(next_tile, 0)
            current_tile = next_tile
         
        else:
            h[next_tile] = h.get(next_tile, 0) + 1         
            current_tile = (0,0)

print(sum([x for x in h.values() if (x % 2) == 1]))

#part 2

def part_2(tile, tile_colours, directions):
    
    black = sum([tile_colours.get((tile[0] + d[0], tile[1] + d[1]), 0) % 2 for d in directions])

    tile_colour = tile_colours[tile] % 2

    if (tile_colour == 1) & ((black == 0) | (black > 2)):
            return 0
    elif (tile_colour == 0) & (black == 2):
            return 1
    else:
        return tile_colour
    
        
for day in range(100):
    
    new_h = {}

    #extend h 
    east_and_west = max([abs(x[0]) for x in h.keys()]) + 2
    north_and_south = max([abs(x[1]) for x in h.keys()]) + 2
    for i in range(-east_and_west, east_and_west):
        for j in range(-north_and_south, north_and_south):
            h[(i,j)] = h.get((i,j), 0)
    
    for tile, colour in h.items():
        new_h[tile] = part_2(tile, h, moves.values())
    
    h = new_h
    
print(sum(h.values()))