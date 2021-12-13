import matplotlib.pyplot as plt

f = open('input.txt')
raw = f.readlines()
f.close()

grid = {}
folds = []

lines = list(raw)
for line in lines:
    if line[0].isnumeric():
        line = [int(x) for x in line.strip().split(',') if x != '']
        grid[(line[0], line[1])] = 1
        
    if line[0] == 'f':
        folds = folds + [line.strip().replace('fold along ', '').split('=')]

marked = []

for fold in folds:
    
    folded_grid = {}
    fold_at = int(fold[1])
    
    for k, v in grid.items():
    
        if fold[0] == 'y':
            folded_k = (k[0], int((2*fold_at - k[1])))
            to_fold = k[1] >= fold_at
            
        elif fold[0] == 'x':
            folded_k = (int((2*fold_at - k[0])), k[1])
            to_fold = k[0] >= fold_at
            
        new_value = min(1, grid[k] + grid.get(folded_k, 0))
        
        if to_fold:
            folded_grid[folded_k] = new_value
        else:
            folded_grid[k] = new_value

    grid = folded_grid.copy()
    marked += [sum(folded_grid.values())]

print(marked[0])

x = [i[0] for i in grid.keys()]
y = [j[1] for j in grid.keys()]
plt.scatter(x, y, marker='*', s=500, c='gold')
plt.gca().invert_yaxis()
plt.show()