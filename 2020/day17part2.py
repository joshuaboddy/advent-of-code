with open('day17input.txt', 'r') as file:
    
    input = [line.strip() for line in file]
    
    d = {}
    
    #parse input
    for row, line in enumerate(input):
        for column, char in enumerate(list(line)):
            d[(column, row, 0, 0)] = char
            
def neighbours(dic,x,y,z,w):
    active = 0
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            for c in [-1,0,1]:
                for d in [-1,0,1]:
                    if a==0 and b==0 and c==0 and d==0:
                        continue
                    elif (x+a, y+b, z+c, w+d) in dic.keys():
                        if dic[x+a,y+b,z+c, w+d] == '#':
                            active+=1
    return active

i=0
while i < 6:
    new_d = {}
    for key in d:
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for z in [-1,0,1]:
                    for w in [-1,0,1]:
                        lookup = (key[0] + x, key[1] + y, key[2] + z, key[3] + w)
                        n = neighbours(d, key[0] + x, key[1] + y, key[2] + z, key[3] + w)
                        if (d.get(lookup, '.') == '#') and (n==2 or n==3): 
                            new_d[lookup] = '#'
                        elif (d.get(lookup, '.') == '.') and (n==3):
                            new_d[lookup] = '#'
                        else:
                            new_d[lookup] = '.'
    i+=1
    d = new_d 
    
print(sum([1 for x,k in d.items() if (k == '#')]))

