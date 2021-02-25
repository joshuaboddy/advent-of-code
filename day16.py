with open('day16instructions.txt', 'r') as file:
    
    input = [rng.split('-') for line in file for rng in line.strip().replace(' or ', ':').split(':')[1:]]
    
    set_of_ranges = set()
    for rng in input:
        set_of_ranges = set_of_ranges.union([i for i in range(int(rng[0]), int(rng[1])+1)])
        
with open('day16nearbytickets.txt', 'r') as nearby_file:
    
    part_1 = sum([int(x) for line in nearby_file for x in line.strip().split(',') if int(x) not in set_of_ranges])
    
    print(part_1)
    
    
    
    