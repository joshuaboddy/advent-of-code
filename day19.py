import re

with open('day19rulespart2.txt', 'r') as file: #update this to day19rules.text for part 1, day19rulespart2.txt for part 2
    
    input = [line.replace('"','').strip().split(': ') for line in file]
    
rules = {}
for rule in input:
    rules[rule[0]] = rule[1]
    
start = ['0']
string = " " + rules['0'] + " "

i = 0

checker = True

while checker:
    for idx in start:  
        rule = rules[idx]
        string = string.replace(" " + idx + " ", " ( " + rule + " ) ")

        start = set([s for s in string.split(" ") if s.isnumeric()])
        
        if len([s for s in string if s.isnumeric()]) == 0:
            checker = False
       
       #only needed for part 2, works with part 1 still though
        if idx == '8' or idx == '11':
            i+=1
        if i > 6:
            rules['8'] = '42'
            rules['11'] = '42 31'

final_string = string.replace(" ", "")

with open('day19strings.txt', 'r') as wordfile:
    
    ans = sum([re.fullmatch(final_string, line.strip()) is not None for line in wordfile])
    
print(ans)
