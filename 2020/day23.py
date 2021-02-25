import collections

input = '418976235'

cups = [int(char) for char in input]

move1 = 0

while move1 <= 99:
    move = move1 % len(cups)
    current_cup = cups[move]
    cups_to_move = []
    for ind in range(move+1, move+4):
        if ind <= len(cups) - 1:
            cups_to_move.append(cups[ind])
        else:
            cups_to_move.append(cups[ind % len(cups)])
    
    dest_find = True
    i=1
    while dest_find:
        if current_cup - i < 1:
            dest_cup = max([cup for cup in cups if cup not in cups_to_move])
            dest_find = False
        elif current_cup - i not in cups_to_move:
            dest_cup = current_cup - i
            dest_find = False
        else:
            i+=1
            
    new_cups = [cup for cup in cups if cup not in cups_to_move]
    move_cups_to = new_cups.index(dest_cup)
    for i in [1,2,3]:
        pos = move_cups_to + i

        new_cups.insert(pos, cups_to_move[i-1])
        
    shift = move - new_cups.index(current_cup)
    
    new_cups = collections.deque(new_cups)
    new_cups.rotate(shift)
      
    cups = list(new_cups)
    move1+=1
    
print(cups)

shift = -cups.index(1)
cups = collections.deque(cups)
cups.rotate(shift)
cups = list(cups)
string = ''
for cup in cups:
    if cup != 1:
        string = string + str(cup)
print(string)
    