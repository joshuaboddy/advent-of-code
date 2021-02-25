import collections
import itertools
import time

start_time = time.time()

with open('day22input.txt', 'r') as file: #update this to day19rules.text for part 1, day19rulespart2.txt for part 2
    
    input = [line.strip() for line in file]
        
def get_cards(players_and_cards):
    
    p1 = collections.deque()
    p2 = collections.deque()

    p2_start = players_and_cards.index('Player 2:')
    
    for enum, card in enumerate(players_and_cards):
        if card.isnumeric(): 
            if enum < p2_start:
                p1.append(int(card))
            else:
                p2.append(int(card))
    
    return p1, p2

def bigger_card(p1, p2):
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
    
    return p1, p2

def sub_game_start(p1, p2):
    c1 = p1[0]
    p1.popleft()
    p1 = collections.deque(itertools.islice(p1, 0, c1))
    
    c2 = p2[0]
    p2.popleft()
    p2 = collections.deque(itertools.islice(p2, 0, c2))

    return p1, p2

def round_winner(p1, p2):
    
    c1 = p1[0]
    c2 = p2[0]


    if len(p1) <= c1 or len(p2) <= c2:
        return bigger_card(p1, p2)
    else:
        new_p1, new_p2 = sub_game_start(p1, p2)
        gw = game_winner(new_p1, new_p2)[0]
        if gw == 'p1':
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
            
        return p1, p2
    
def game_winner(p1, p2):

    dict_per_game = {}

    i = 0    

    while len(p1) * len(p2) > 0:        
        dict_per_game[i] = (list(p1), list(p2))
        p1, p2 = round_winner(p1, p2) 
        if (list(p1), list(p2)) in dict_per_game.values():
            return 'p1', p1
        i+=1
        
    if len(p1) == 0:
        return 'p2', p2
    else:
        return 'p1', p1


p1, p2 = get_cards(input)

print('part 2 is ' + str(sum([(enum+1)*card for enum,card in enumerate(reversed(game_winner(p1, p2)[1]))])))

print(time.time() - start_time, "seconds")

            
    