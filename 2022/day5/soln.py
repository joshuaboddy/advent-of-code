import re

f = open('input.txt')
raw = f.readlines()
f.close()

part = 2
crates = {}
for line in raw:
    if line[:4] != "move" and line[:2] != " 1":
        letters = line[1::4]
        for idx, letter in enumerate(letters):
            if letter != ' ':
                crates[idx + 1] = crates.get(idx + 1, []) + [letter]
                
    
    elif line[:4] == "move":
        moves = [int(i) for i in re.findall(r'\d+', line.strip())]
        
        crates_to_move = crates[moves[1]][:moves[0]]
        if part == 1:
            crates_to_move = crates_to_move[::-1]
            
        crates[moves[2]] = crates_to_move + crates[moves[2]] 
        crates[moves[1]] = crates[moves[1]][moves[0]:]
        
sorted_crates = dict(sorted(crates.items()))
message = ''.join([x[0] for x in sorted_crates.values()])
print(message)
