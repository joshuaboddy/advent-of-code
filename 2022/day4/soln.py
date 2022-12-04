import re

f = open('input.txt')
raw = f.readlines()
f.close()

part1 = 0
part2 = 0
for line in raw:
    int_strings = re.findall(r'\d+', line)
    ints = [int(i) for i in int_strings]
    range1 = set(range(ints[0], ints[1] + 1))
    range2 = set(range(ints[2], ints[3] + 1))
    
    range_union = range1.union(range2)
    if range_union in [range1, range2]:
        part1 += 1
        
    range_intersection = range1.intersection(range2)
    if range_intersection:
        part2 += 1
        