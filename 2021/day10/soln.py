import numpy as np

f = open('input.txt')
raw = f.readlines()
f.close()

def char_in(syntax, chars):

    return [char for char in chars if char in syntax]

doubles = ['<>','()','[]','{}']
left = ['<','(','[','{']
right = ['>',')',']','}']
    
error_values = [25137, 3, 57, 1197]
error_lookup = dict(zip(right, error_values))    

complete_values = [4,1,2,3]
complete_lookup = dict(zip(left, complete_values))

corrupt = {}
p2scores = []

lines = list(raw)
for line in lines:
    line = line.strip()
    
    to_replace = char_in(line, doubles)
    while len(to_replace) > 0:
        for r in to_replace:
            line = line.replace(r, '')
            to_replace = char_in(line, doubles)
    
    rights = char_in(line, right)
    if len(rights) > 0:
        found = line[min([line.index(r) for r in rights])]
        corrupt[found] = corrupt.get(found, 0) + 1
        
    else:
        p2line = 0
        reverse_line = line[::-1]
        for symbol in reverse_line:
            p2line = p2line*5 + complete_lookup[symbol]

        p2scores.append(p2line)

p1 = sum([corrupt[key]*error_lookup[key] for key in corrupt.keys() & error_lookup.keys()])
p2 = np.median(p2scores)

print(p1, p2)