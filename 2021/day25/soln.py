f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)
coords = {}

for y_coord, line in enumerate(lines):
    x_values = line.strip()
    for x_coord, x in enumerate(x_values):
        coords[(x_coord, y_coord)] = x
        
coords = dict(sorted(coords.items(), key=lambda item: item[1]))
        
new_coords = {}
i = 0

xs = max([a[0] for a in coords.keys()])+1
ys = max([a[1] for a in coords.keys()])+1

while True:
    i+=1
    new_coords = {}
    prev_coords = coords.copy()
    for k, v in dict(filter(lambda coord: coord[1] == '>', coords.items())).items():
        next_pos = ((k[0] + 1) % xs, k[1])
        if coords.get(next_pos, '.') == '.':
            new_coords[next_pos] = '>'
            new_coords[k] = '.'
        else:
            new_coords[k] = '>'
                
    for k, v in dict(filter(lambda coord: coord[1] == 'v', coords.items())).items():         
        next_pos = (k[0], (k[1] + 1) % ys)
        if new_coords.get(next_pos, coords.get(next_pos, '.')) == '.':
            new_coords[next_pos] = 'v'
        else:
            new_coords[k] = 'v'

    coords = new_coords.copy()

    if coords == prev_coords:
        print(i)
        break
    