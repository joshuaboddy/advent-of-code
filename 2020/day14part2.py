with open('day14input.txt', 'r') as file:
    
    input = [line.strip() for line in file]
    
    current_mask = ''
    value = ''
    
    d = {}
    for line in input:
        if line[:4] == 'mask':
            current_mask = line[7:]
        else:
            value = int(line[line.find('=')+2:])
            mem = int(line[line.find('[')+1:line.find(']')])
                           
            binary_rep = bin(mem)[2:].zfill(36)
            
            final_rep = ''
            
            for enum, char in enumerate(current_mask):
                if char != '0':
                    final_rep += char
                else:
                    final_rep += binary_rep[enum]
            
            X_count = final_rep.count('X')
            
            bins = [bin(i)[2:] for i in range(2**X_count)]
            bins = [x.zfill(X_count) for x in bins]
                        
            for x in bins:
                new_final_rep = ''
                cnt = 0
                for char in final_rep:
                    if char == 'X':
                        new_final_rep += x[cnt]
                        cnt+=1
                    else:
                        new_final_rep += char
                
                new_final_rep = int(new_final_rep, 2)
                d[new_final_rep] = value

    print(sum(d.values()))            

    
