f = open("input.txt", "r")
lines = [[char for char in line.strip() if char.isnumeric()] for line in f.readlines()]

part1 = sum([int(line[0] + line[-1]) for line in lines])

print(part1)


replacer = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
    }


part2 = 0
f = open("input.txt", "r")
for line in f.readlines():
    for n_string in replacer:
        line = line.replace(n_string, f"{n_string}{replacer[n_string]}{n_string}")
    
    chars = [char for char in line if char.isnumeric()]

    part2 += int(chars[0] + chars[-1]) 
    
print(part2)