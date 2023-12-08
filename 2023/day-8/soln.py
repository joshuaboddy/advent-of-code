import math
import re


def chase_map(map_dict, moves, node, check_digits):
    
    i = 0
    while node[-check_digits:] != 'Z' * check_digits:
        move = moves[i % len(moves)]
        node = map_dict[node][move]
        i += 1
    
    return i


f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

moves = lines[0]
map_dict = {}

for line in lines[2:]:
    nodes = line.split(' = ')
    left_and_right = re.findall('[A-Z]+', nodes[1])
    
    map_dict[nodes[0]] = {
        'L': left_and_right[0], 
        'R': left_and_right[1]
        }
    

# part 1
print(chase_map(map_dict, moves, 'AAA', 3))

 
# part 2
a_nodes = [node for node in map_dict if node[-1] == "A"]
moves_to_z = []
for a_node in a_nodes:
    moves_to_z.append(chase_map(map_dict, moves, a_node, 1))

print(math.lcm(*moves_to_z))
