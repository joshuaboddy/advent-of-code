import re

f = open('2016/Day 2/input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

move_dict = {'U':[-1,0], 'L':[0,-1], 'D':[1,0], 'R':[0,1]}

start = [2,0]
code = ''

keypad = [['x', 'x', '1', 'x', 'x'],
          ['x', '2', '3', '4', 'x'],
          ['5', '6', '7', '8', '9'],
          ['x', 'A', 'B', 'C', 'x'],
          ['x', 'x', 'D', 'x', 'x']]

for line in lines:
    moves = re.findall('[A-Z]', line)
    for move in moves:
        next_position = [start[0] + move_dict[move][0], start[1] + move_dict[move][1]]
        if 0 <= next_position[0] < 5 and 0 <= next_position[1] < 5:
            if keypad[next_position[0]][next_position[1]] != 'x':
                start = next_position
    code += keypad[start[0]][start[1]]

print(code)