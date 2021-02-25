import pandas as pd 
from collections import Counter

with open("day6input.txt") as file:
    
    lines = [lines.replace("\n", " ") for lines in file.read().split("\n\n")]

    part1summer = 0
    part2summer = 0
    for line in lines:
        lineset = set(line)
        try:
            lineset.remove(' ')
        except:
            lineset
        part1summer+=len(lineset) 
    
        word_count = len(line.split())
        letter_count = Counter(line)
        ser = pd.Series(letter_count)
        ser = ser[ser.index != ' ']
        part2summer+=sum(ser == word_count)
   
    print(part1summer) 
    print(part2summer)

