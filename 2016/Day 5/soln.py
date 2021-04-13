import hashlib

puzzle_input = 'wtnhxymk'
i = 0
part1 = ''
part2 = {}
while len(part2) < 8:
    s = puzzle_input + str(i)
    result = hashlib.md5(s.encode()).hexdigest()
    if result[0:5] == '00000':
        if len(part1) < 8:
            part1=part1+result[5]
            
        position = result[5]
        if position.isdigit():
            if int(position) < 8:
                if int(position) not in part2.keys():
                    part2[int(position)] = result[6]
    i=i+1
print(part1)
print(''.join([part2[i] for i in sorted(part2)]))