import re

f = open("test.txt", "r")
lines = [line.strip() for line in f.readlines()]

def part1(lines):
    
    seeds =  [int(x) for x in re.findall(r'\d+', lines[0])]
    lowest_answer = 0
    
    for seed in seeds:
        for line in lines[1:]:
            if "map" in line:
                found_match_in_map = False
                
            elif line and not found_match_in_map:
                ranges =  [int(x) for x in re.findall(r'\d+', line)]
                if seed in range(ranges[1], ranges[1] + ranges[2] + 1):
                    seed = ranges[0] + seed - ranges[1]
                    found_match_in_map = True
                    
        lowest_answer = seed if lowest_answer == 0 or seed < lowest_answer else lowest_answer
        
    return lowest_answer
    


def part2(lines):
    
    seeds =  [int(x) for x in re.findall(r'\d+', lines[0])]
    seed_ranges = [(seeds[2*i], seeds[2*i] + seeds[2*i + 1]) for i in range(int(len(seeds) / 2))]
    
    reverse_lines = lines[::-1]
    
    lowest_location = 0
    initial_location = lowest_location
    
    while True:
        found_match_in_map = False
        
        for line in reverse_lines:
            locations =  [int(x) for x in re.findall(r'\d+', line)]
            
            if line:          
                if "seeds" in line:
                    for seed_range in seed_ranges:
                        if seed_range[0] <= lowest_location < seed_range[1] :
                            return initial_location
                            
                    lowest_location = initial_location + 1
                    initial_location = lowest_location
                
                elif "map" in line:
                    found_match_in_map = False
                
                elif locations and not found_match_in_map:
                    if locations[0] <= lowest_location < locations[0] + locations[2]:
                        lowest_location = locations[1] + lowest_location - locations[0]
                        found_match_in_map = True

print(part1(lines))
print(part2(lines))