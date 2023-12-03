import math

f = open("input.txt", "r")
lines = f.readlines()

rules = {
    "red": 12,
    "green": 13,
    "blue": 14
    }

valid_games = 0
powers = 0
for idx, line in enumerate(lines, 1):
    line = line.strip()
    line = line.split(';')
    
    number_of_cubes_needed = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    valid_sets = []
    for game_set in line:
        game_set = game_set.split(',')

        valid_set = True
        for cubes in game_set:
            for colour in rules:
                if colour in cubes:
                    max_allowed_cubes = rules[colour]
                    number_of_cubes = [int(s) for s in cubes.split() if s.isdigit()][0]
                    
                    # part 1 
                    if number_of_cubes > max_allowed_cubes:
                        valid_set = False
                        
                    # part 2
                    if number_of_cubes > number_of_cubes_needed[colour]:
                        number_of_cubes_needed[colour] = number_of_cubes
                              
        valid_sets.append(valid_set)

    valid_games += idx if all(valid_sets) else 0
    powers += math.prod(number_of_cubes_needed.values())

print(valid_games)
print(powers)