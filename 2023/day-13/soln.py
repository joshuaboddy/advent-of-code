def flip_patterns(patterns):
    
    flipped_patterns = []
    
    for pattern in patterns:
        flipped_pattern = []
        for x in range(len(pattern[0])):
            flipped_column = ''
            for y in range(len(pattern)):
                flipped_column += pattern[y][x]
            
            flipped_pattern.append(flipped_column)
            
        flipped_patterns.append(flipped_pattern)
    
    return flipped_patterns     


def smudge_pattern(pattern, y, x):
    
    replacer = {'.': '#', '#': '.'}
    
    smudged_pattern = pattern[0:y] + pattern[y+1:]
    smudger = pattern[y][0:x] + replacer[pattern[y][x]] + pattern[y][x+1:]
    smudged_pattern.insert(y, smudger)
    
    return smudged_pattern


def summarize(patterns, multiplier, part2):
    
    total = 0
    
    for idx, pattern in enumerate(patterns):
        str_length = len(pattern[0])
        
        not_found = True
        
        for y in range(len(pattern)):
            for x in range(len(pattern[y])):
                smudged_pattern = smudge_pattern(pattern, y, x) if part2 else pattern
                i = 0
                
                while not_found and i < str_length - 1:
                    for j in [0, i]:
                        if (i - j) <= x < (str_length - j) or not part2:
                            if len(smudged_pattern[0][i-j:str_length-j]) % 2 == 0:
                                if any([line[i-j:str_length-j] != line[i-j:str_length-j][::-1] for line in smudged_pattern]):
                                    continue
                                else:
                                    total += multiplier * (i - j + len(pattern[0][i-j:str_length-j])/2)
                                    not_found = False
                                    break
                        
                    i += 1
            
    return total


def rows_and_columns_total(patterns, part2=False):

    column_total = summarize(patterns, 1, part2)
    flipped_patterns = flip_patterns(patterns)
    row_total = summarize(flipped_patterns, 100, part2)
    
    return column_total + row_total



f = open("input.txt", "r")

lines = f.readlines()

patterns = []
i = 0
for line in lines:

    line = line.strip()
    if line == "":
        i += 1    
    else:
        if len(patterns) <= i:
            patterns.insert(i, [])
        
        patterns[i].append(line)

print(rows_and_columns_total(patterns, part2=True))