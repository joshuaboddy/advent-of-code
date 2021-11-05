import re

f = open('input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

d = {}
i = {}

for line in lines:

    #parse
    letters = re.findall('[a-zA-Z]+', line)
    sector_id = re.findall('-?\d+', line)
    
    if 'value ' in line:
        val = re.findall('-?\d+', line)
        bot = 'bot ' + val[1]
        if bot in d.keys():
            d[bot] = d[bot] + [int(val[0])]
        else:
            d[bot] = [int(val[0])]
    else:
        inst = line.strip().replace(' and high to ', ' gives low to ').split(' gives low to ')
        i[inst[0]] = [inst[1], inst[2]]

while 'output 0' not in d.keys() or 'output 1' not in d.keys() or 'output 2' not in d.keys():
    bot = ''
    val = []
    for b, v in d.items():
        if len(v) == 2:
            if sorted(v) == [17, 61]:
                print('part 1 is ' + b)
            bot = b
            val = v
            break
        
    if i[bot][0] in d.keys():
        d[i[bot][0]] = d[i[bot][0]] + [min(val)]
    else:
        d[i[bot][0]] = [min(val)]
    if i[bot][1] in d.keys():
        d[i[bot][1]] = d[i[bot][1]] + [max(val)]
    else:
        d[i[bot][1]] = [max(val)]
    d[bot] = []
    
print('part 2 is ' + str(d['output 0'][0] * d['output 1'][0] * d['output 2'][0]))
            
