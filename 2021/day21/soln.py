import itertools 

p1, p2 = 10, 2
p1score, p2score = 0, 0

die = 1
cntr = 0

while p1score < 1000 and p2score < 1000:
    
    roll = 3*(die % 100 + 1)
    if cntr % 2 == 0:    
        p1 = (p1 + roll - 1) % 10 + 1
        p1score+=p1
        
    else:
        p2 = (p2 + roll - 1) % 10 + 1
        p2score+=p2

    die += 3
    cntr += 1
    
print(min(p1score, p2score) * (die-1))


quantum_rolls_and_freq = {}
for prod in itertools.product([1,2,3], repeat=3):
    quantum_rolls_and_freq[sum(prod)] = quantum_rolls_and_freq.get(sum(prod), 0) + 1
    
pos1, pos2 = 10, 2
universes = {((0, pos1), (0, pos2), 0): 1}
chicken_dinner = {0: 0, 1: 0}

while len(universes) > 0:
    
    prev_universes = universes.copy() 
    universes = {}
    
    for prev_game_state, prev_freq in prev_universes.items():
        
        player_to_roll = prev_game_state[2] 
        prev_score, prev_pos = prev_game_state[player_to_roll]

        for roll, freq in quantum_rolls_and_freq.items():
            this_pos = (prev_pos + roll - 1) % 10 + 1			
            this_score = prev_score + this_pos
            
            if this_score > 20:
                chicken_dinner[player_to_roll] += prev_freq * freq
                continue
            
            next_roller = (player_to_roll + 1) % 2       
            game_state = [0,0,0]
            game_state[player_to_roll] = (this_score, this_pos)	
            game_state[2] = next_roller 
            game_state[next_roller] = prev_game_state[next_roller]
                         
            universes[tuple(game_state)] = universes.get(tuple(game_state), 0) + prev_freq * freq
            
print(max(chicken_dinner.values()))