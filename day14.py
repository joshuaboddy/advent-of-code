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
                           
            binary_rep = bin(value)[2:].zfill(36)

            final_rep = ''
            
            for enum, char in enumerate(current_mask):
                if char != 'X':
                    final_rep += char
                else:
                    final_rep += binary_rep[enum]
            
            d[mem] = int(final_rep,2)

print(sum(d.values()))
    
