import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

f = open('input.txt')
raw = f.readlines()
f.close()

part1 = 0
for line in raw:
    line = line.strip()
    c1 = line[:int(len(line)/2)]
    c2 = line[int(len(line)/2):]
    
    common_item = set(c1).intersection(set(c2)).pop()
    part1 += alphabet.index(common_item) + 1
    
print(part1)


part2 = 0
for i, line in enumerate(raw):
    line = line.strip()
    if i % 3 == 0:
        common_item = set(line)
    else:
        common_item = common_item.intersection(set(line))
        
    if i % 3 == 2:
        part2 += alphabet.index(common_item.pop()) + 1

print(part2)