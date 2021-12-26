import re

def cube_intersect(c1, c2):

    return all([x >= y for x, y in zip(c1[1], c2[0])]) & all([x <= y for x, y in zip(c1[0], c2[1])])

def split_cube(c1, middle_cube):
    
    split_cubes = []
    
    c1_start = c1[0]
    c1_end = c1[1]
    
    if middle_cube[1][2] < c1_end[2]:
        c1_top = ((c1_start[0], c1_start[1], middle_cube[1][2] + 1), c1_end)
        split_cubes = split_cubes + [c1_top]
        
    if middle_cube[0][2] > c1_start[2]:        
        c1_bottom = (c1_start, (c1_end[0], c1_end[1], middle_cube[0][2] - 1))
        split_cubes = split_cubes + [c1_bottom]
        
    if middle_cube[0][0] > c1_start[0]:
        c1_front = ((c1_start[0], c1_start[1], middle_cube[0][2]), (middle_cube[0][0] - 1, c1_end[1], middle_cube[1][2]))
        split_cubes = split_cubes + [c1_front]
    
    if middle_cube[1][0] < c1_end[0]:
        c1_back = ((middle_cube[1][0] + 1, c1_start[1], middle_cube[0][2]), (c1_end[0], c1_end[1], middle_cube[1][2]))
        split_cubes = split_cubes + [c1_back]
    
    if middle_cube[0][1] > c1_start[1]:
        c1_left = ((middle_cube[0][0], c1_start[1], middle_cube[0][2]), (middle_cube[1][0], middle_cube[0][1] - 1, middle_cube[1][2]))
        split_cubes = split_cubes + [c1_left]
    
    if middle_cube[1][1] < c1_end[1] :
        c1_right = ((middle_cube[0][0], middle_cube[1][1] + 1, middle_cube[0][2]), (middle_cube[1][0], c1_end[1], middle_cube[1][2]))
        split_cubes = split_cubes + [c1_right]  
  
    return tuple(split_cubes)

def middle_cube_finder(c1, c2):
    
    c1_start = c1[0]
    c1_end = c1[1]
    
    c2_start = c2[0]
    c2_end = c2[1]
    
    middle_cube = (tuple([max(x,y) for x,y in zip(c1_start, c2_start)]), tuple([min(x,y) for x,y in zip(c1_end, c2_end)]))
    
    return middle_cube

def cube_vol(cube):
    
    return (cube[1][0] - cube[0][0] + 1) * (cube[1][1] - cube[0][1] + 1) * (cube[1][2] - cube[0][2] + 1)

f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)
seen_cubes = []

part1 = False

for line in lines:

    line = line.strip()
    switch = 'on' if 'on' in line else 'off'
    nums = [int(i) for i in re.findall('-?\d+', line)]
    
    if part1:
        if not all([-50 <= x <= 50 for x in nums]):
            continue
        
    this_cube = (tuple(nums[0::2]), tuple(nums[1::2]))
    
    split_cubes = []
    
    for existing_cube in seen_cubes:
        if cube_intersect(existing_cube, this_cube):
            for subcube in split_cube(existing_cube, middle_cube_finder(this_cube, existing_cube)):
                split_cubes.append(subcube)
        else:
            split_cubes.append(existing_cube)
            
    seen_cubes = split_cubes
                
    if switch == 'on':
        seen_cubes.append(this_cube)
            
print(sum([cube_vol(cube) for cube in seen_cubes]))