import re

f = open('input.txt')
raw = f.readlines()
f.close()

#part 1
depth = 0
horizontal = 0

lines = list(raw)
for line in lines:
    
    line = line.strip()
    words = line.split()[0]
    ints = int(re.findall('-?\d+', line)[0])
    
    if words == 'up':
        depth = depth - ints
    elif words == 'down':
        depth = depth + ints
    else:
        horizontal = horizontal + ints
        
print(depth*horizontal)

#part 2
depth = 0
horizontal = 0
aim = 0

for line in lines:
    
    line = line.strip()
    words = line.split()[0]
    ints = int(re.findall('-?\d+', line)[0])
    
    if words == 'up':
        aim = aim - ints
    elif words == 'down':
        aim = aim + ints
    else:
        horizontal = horizontal + ints
        depth = depth + aim * ints
        
print(depth*horizontal)