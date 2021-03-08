import re

f = open('2016/Day 1/input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)
#lines = ['R8', 'R4', 'R4', 'R8']
directions = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}
angle = 0
coordinate = [0, 0]
ends_visited = [0,0]
coords_visited = [[0,0]]
visited_twice = False

for line in lines:
    turns = re.findall('[A-Z]', line)
    distances = re.findall('-?\d+', line)
    distances = [int(x) for x in distances]

    for turn, distance in zip(turns, distances):
        if turn == 'R':
            angle = (angle + 90) % 360
        else: 
            angle = (angle - 90) % 360


        for i in range(1,distance+1):
            coord_x = coordinate[0] + (directions[angle][0] * i)
            coord_y = coordinate[1] + (directions[angle][1] * i)
            
            if visited_twice == False:
                if [coord_x, coord_y] in coords_visited:
                    print('part 2 is: ' + str(sum([abs(x) for x in [coord_x, coord_y]])))
                    visited_twice = True
                else:
                    coords_visited = coords_visited + [[coord_x, coord_y]]

        coordinate[0] = coordinate[0] + (directions[angle][0] * distance)
        coordinate[1] = coordinate[1] + (directions[angle][1] * distance)
        
print('part 1 is: ' + str(sum([abs(x) for x in coordinate])))

