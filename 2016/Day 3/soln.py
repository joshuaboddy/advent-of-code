import re

f = open('2016/Day 3/input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

p1_triangles = 0
p2_triangles = 0
cntr = 0

for line in lines:
    triangles = re.findall('-?\d+', line)
    triangles = sorted([int(x) for x in triangles])
    if triangles[0] + triangles[1] > triangles[2]:
        p1_triangles+=1
    
    if cntr % 3 == 0:
        col1tri = []
        col2tri = []
        col3tri = []
    
    row = re.findall('-?\d+', line)
    row = [int(x) for x in row]
    col1tri+=[row[0]]
    col2tri+=[row[1]]
    col3tri+=[row[2]]

    if cntr % 3 == 2:
        for tri in [col1tri, col2tri, col3tri]:
            tri = sorted(tri)
            if tri[0] + tri[1] > tri[2]:
                p2_triangles+=1
    
    cntr+=1
    
print('part 1 is: ' + str(p1_triangles))
print('part 2 is: ' + str(p2_triangles))