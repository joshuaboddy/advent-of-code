import pandas as pd

with open('day11input.txt', 'r') as file:
    
    input = [chars for line in file for chars in line.split()]
    
    d = {}
    
    for row, line in enumerate(input):
        for column, letter in enumerate(line):
            d[(row, column)] = letter
            
    def good_get(mydict, key):
        if key in mydict:
            output = mydict[key]
        else:
            output = None
        return output
    
   
    direct = dict([
                    (0, (1,0)),
                    (1, (-1, 0)),
                    (2, (1, 1)),
                    (3, (-1, 1)),
                    (4, (1, -1)),
                    (5, (-1, -1)),
                    (6, (0, 1)),
                    (7, (0, -1))                 
                   ])
   
    run=True    
    while run:

        next_dict = {}
        
        not_dots = [a for a,b in d.items() if b != '.']    
                
        for el in d:
            row = el[0]
            col = el[1]
            letter = d[el]

            closest = []
            for i in range(len(direct)):
                
                n=1
                seat_finder=True
                
                while seat_finder:
                    next_char = good_get(d, (row + n*direct[i][0], col + n*direct[i][1]))
                    if next_char == '.':
                        n+=1
                    else:
                        closest.append(next_char)
                        seat_finder=False
                                
                num_adj = closest.count('#') 
        
        
                if d[el] == '.':
                    next_dict[el] = '.'
                elif num_adj == 0:
                    next_dict[el] = '#'
                elif d[el] == '#' and num_adj >= 5:
                    next_dict[el] = 'L'
                else:
                    next_dict[el] = d[el]
    
        if next_dict == d:
            print(sum([1 for value in d.values() if value == '#']))
            run = False
        else: 
            d = next_dict