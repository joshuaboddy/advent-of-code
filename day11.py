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
    
   
    run=True    

    while run:

        next_dict = {}
        
        not_dots = [a for a,b in d.items() if b != '.']    
                
        for el in not_dots:
            row = el[0]
            col = el[1]
            letter = d[el]
            
            adjacent = [
                        good_get(d, (row-1, col)),
                        good_get(d, (row-1, col+1)),
                        good_get(d, (row-1, col-1)),
                        good_get(d, (row, col+1)),
                        good_get(d, (row, col-1)),
                        good_get(d, (row+1, col)),
                        good_get(d, (row+1, col+1)),
                        good_get(d, (row+1, col-1))
                        ]
            
            num_adj = adjacent.count('#') 

            if num_adj == 0:
                next_dict[el] = '#'
            elif d[el] == '#' and num_adj >= 4:
                next_dict[el] = 'L'
            else:
                next_dict[el] = d[el]
            

        if next_dict == d:
            print(sum([1 for value in d.values() if value == '#']))
            run = False
        else: 
            d = next_dict