import numpy as np

f = open('input.txt')
raw = f.readlines()
f.close()

d = {}

lines = list(raw)
for y_coord, line in enumerate(lines):
    x_values = [int(num) for num in line.strip()]
    for x_coord, x in enumerate(x_values):
        d[(x_coord, y_coord)] = x

def get_nbhd(pos, d):
    
    pos_x = pos[0]
    pos_y = pos[1]
    
    nbhd = []
    
    for coord in [[0,0], [0,1], [1,0], [0,-1], [-1,0]]:
        i = coord[0]
        j = coord[1]
        if (pos_x + i, pos_y + j) in d.keys():
            nbhd = nbhd + [(pos_x + i, pos_y + j)]
                
    return nbhd


def check_basin_is_not_full(basin, d):
    
    for point in basin: 
        for nbr in get_nbhd(point, d):
            if nbr not in basin and d.get(nbr, 0) != 9:
                return True 
    
    return False


def get_basins(lowpoint, d):
    
    basin = [lowpoint]

    while check_basin_is_not_full(basin, d):
        for point in basin:
            for nbr in get_nbhd(point, d):
                if nbr not in basin and d[nbr] != 9:
                    basin = basin + [nbr]
    return basin

#part 1
part1 = 0  
lowpoints = []

for key in d.keys():
    cnt=0
    
    for nbr in get_nbhd(key, d):
        if nbr != key:
            if d[key] < d[nbr]:
                cnt += 1
                
    if cnt == (len(get_nbhd(key, d))-1):
        part1 += d[key]+1
        lowpoints = lowpoints + [key]

print(part1)

#part 2  
basins = {}
nbs = []
  
for lowpoint in lowpoints:
    basins[lowpoint] = len(get_basins(lowpoint, d))

print(np.prod(sorted(basins.values(), reverse=True)[:3]))