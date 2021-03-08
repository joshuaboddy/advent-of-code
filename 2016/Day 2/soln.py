import re

f = open('2016/Day 2/input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

move_dict = {'U':-3, 'L':-1, 'D':3, 'R':1}

start = 5
code = ''

for line in lines:
    moves = re.findall('[A-Z]', line)
    for move in moves:
        Rmax = int((start-1)/3)*3 + 3
        Lmin = int((start-1)/3)*3 + 1
        Dmax = (start-1) % 3 + 7
        Umin = (start-1) % 3 + 1
        if move == 'R':
            start = min(start + 1, Rmax)
        elif move == 'L':
            start = max(start - 1, Lmin)
        elif move == 'U':
            start = max(start - 3, Umin)
        else:
            start = min(start + 3, Dmax)
    code = code + str(start)
print('part 1 is: ' + code)