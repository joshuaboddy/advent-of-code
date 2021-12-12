f = open('input.txt')
raw = f.readlines()
f.close()

paths = {}

lines = [line.strip().split('-') for line in list(raw)]

for line in lines:
    paths[line[0]] = paths.get(line[0], []) + [line[1]]
    paths[line[1]] = paths.get(line[1], []) + [line[0]]
    
for k in paths:
    if 'start' in paths[k]:
        paths[k].remove('start')
    
def part1(cave, been_to):
        
    if cave == 'end':
        return 1
    elif cave.islower():
        been_to.append(cave)
    
    ends = sum([part1(next_cave, been_to) for next_cave in paths[cave] if next_cave not in been_to])
   
    if cave in been_to:
        been_to.remove(cave)
        
    return ends

def part2(cave, been_to):
            
    if cave == 'end':
        return 1
    elif cave.islower():
        been_to.append(cave)
 
    ends = sum([part2(next_cave, been_to) for next_cave in paths[cave] if len(set(been_to)) >= (len(been_to) - 1)])
   
    if cave in been_to:
        been_to.remove(cave)
        
    return ends

print(part1('start', []))
print(part2('start', []))
