with open("day7input.txt") as file:
    
    lines = [lines.replace(' bags', '').replace(' bag', '').replace(' .\n','').split(' contain ') for lines in file]
    
    
    d = {}
    for line in lines:
        d[line[0].strip()] = line[1].replace('.\n','').split(', ')
        
    for a,b in d.items():
        bags = []
        sizes = []
        for bag in b:
            if bag[2:] != ' other' and bag[2:] != ' other.':
                bags.append(bag[2:])
                sizes.append(bag[0])
            d[a] = [bags, sizes]
    
def shiny_gold_recursion(bag_colour):
    if 'shiny gold' in bag_colour:
        return True
    else:
        return any(shiny_gold_recursion(color) for color in d[bag_colour][0])

def bag_number_recursion(bag_colour):
    return sum(int(num) + int(num) * bag_number_recursion(colour) for colour, num in zip(d[bag_colour][0], d[bag_colour][1]))


print(sum(shiny_gold_recursion(colour) for colour in d.keys()) - 1)
print(bag_number_recursion('shiny gold'))