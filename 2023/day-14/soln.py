f = open("test.txt", "r")

lines = [line.strip() for line in f.readlines()]

trans = list(map(list, zip(*lines)))

total = 0

for line in trans:
    dots = 0
    for idx, char in enumerate(line):
        if char == 'O':
            total += ((len(line) - idx)) + dots
        elif char == '.':
            dots += 1
        else:
            dots = 0
            

print(total)
