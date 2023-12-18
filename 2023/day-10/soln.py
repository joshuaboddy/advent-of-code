import numpy as np

def polygon_area(x,y):
        correction = x[-1] * y[0] - y[-1]* x[0]
        main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
        return 0.5*np.abs(main_area + correction)
    

def get_start_pos(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return (y, x)
            

def run_loop(lines, start_dir="U"):
    
    moves = {
        "R": {
            "-": [[(0, 1)], "R"],
            "7": [[ (1, 0)], "D"],
            "J": [[ (-1, 0)], "U"]
            },
        "L": {
            "-": [[(0, -1)], "L"],
            "L": [[ (-1, 0)], "U"],
            "F": [[(1, 0)], "D"]
            },
        "U": {
            "|": [[(-1, 0)], "U"],
            "F": [[ (0, 1)], "R"],
            "7": [[(0, -1)], "L"]
            },
        "D": {
            "|": [[(1, 0)], "D"],
            "L": [[(0, 1)], "R"],
            "J": [[(0, -1)], "L"]
            }
        }
    
    start_pos = get_start_pos(lines)
    node = (start_pos[0] - 1, start_pos[1])
    nodes = [node]
    
    while True:
        if node == start_pos:
            break
        moves_dir = moves[start_dir]
        moves_and_dir = moves_dir[lines[node[0]][node[1]]]
        next_dir = moves_and_dir[1]
        
        for move in moves_and_dir[0]:
            node = (node[0] + move[0], node[1] + move[1])
            start_dir = next_dir
            nodes.append(node)
            
    return nodes
      

f = open("input.txt", "r")

lines = [line.strip() for line in f.readlines()]

nodes = run_loop(lines)

#part 1
print(len(nodes) / 2)

#part 2 shoelace
area = polygon_area(np.array([x[0] for x in nodes]), np.array([x[1] for x in nodes]))
print(area + 1 - len(nodes) / 2)