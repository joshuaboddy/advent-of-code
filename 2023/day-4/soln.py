import re

f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

points = 0
cards = {}
for idx, line in enumerate(lines, 1):
    splitter = line.split('|')
    left = splitter[0].split(':')[1]
    right = splitter[1]
    
    left_nums = re.findall(r'\d+', left)
    right_nums = re.findall(r'\d+', right)
    
    winners = len([right_num for right_num in right_nums if right_num in left_nums])

    if winners:
        points += 2 ** (winners - 1)
        for i in range(1, winners+1):
            cards[idx + i] = cards.get(idx + i, 1) + cards.get(idx, 1)
        
print(points)
print(sum(cards.values()))