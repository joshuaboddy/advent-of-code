with open('day20test.txt', 'r') as file: #update this to day19rules.text for part 1, day19rulespart2.txt for part 2
    
    input = [line.replace('"','').strip().split(': ') for line in file]
