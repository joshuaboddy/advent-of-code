import collections
import copy

with open('day22input.txt', 'r') as file: #update this to day19rules.text for part 1, day19rulespart2.txt for part 2
    
    input = [line.strip() for line in file]
    
    p1 = collections.deque()
    p2 = collections.deque()
    
    p2_start = input.index('Player 2:')
    
    for enum, card in enumerate(input):
        if card.isnumeric(): 
            if enum < p2_start:
                p1.append(int(card))
            else:
                p2.append(int(card))
           
    while len(p1) * len(p2) > 0:
        c1 = p1[0]
        c2 = p2[0]
        p1.popleft()
        p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        if c2 > c1:
            p2.append(c2)
            p2.append(c1)
    
    for seq in [p1, p2]:
        if len(seq) > 0:
            print(sum([(enum+1)*card for enum,card in enumerate(reversed(seq))]))
            
    