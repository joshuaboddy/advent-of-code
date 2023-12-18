def ascii_algo(step):
    cv = 0
    for char in step:
        asc = ord(char)
        cv += asc
        cv *= 17
        cv = cv % 256
        
    return cv


def generate_hashmap(steps):
    
    hashmap = {}
    for step in steps:
        label = step.split("=")[0] if "=" in step else step[:-1]
        box = ascii_algo(label)
    
        
        if box not in hashmap:
            hashmap[box] = {}
            
        if "-" in step:
            remove = step[:-1]
            for key, value in hashmap.items():
                if remove in value:
                    del value[remove]
        elif "=" in step:
            add = step.split("=")[0]
            amount = step.split("=")[1]
    
            hashmap[box][add] = amount 
        
    return hashmap


def calculate_focusing_power(hashmap):
    
    focusing_power = 0
    for box_idx, box in enumerate(hashmap):
        lenses = hashmap[box]
        for lens_idx, lens in enumerate(lenses):
            focusing_power += (box + 1) * (lens_idx + 1) * int(lenses[lens])
            
    return focusing_power


f = open("input.txt", "r")

steps = f.read().strip().split(",")

print(sum([ascii_algo(step) for step in steps]))
print(calculate_focusing_power(generate_hashmap(steps)))
