import collections

with open('day21input.txt', 'r') as file: #update this to day19rules.text for part 1, day19rulespart2.txt for part 2
    
    input = [line.strip().replace(')','').split(' (contains ') for line in file]
    
    d = {}
    
    all_ings = []
    
    for line in input:
        ings = line[0].split(' ')
        allergens = line[1].split(', ')
        
        [all_ings.append(ing) for ing in ings]

        for allergen in allergens:
            if allergen in d:
                d[allergen] = set(d[allergen]).intersection(set(ings))
            else:
                d[allergen] = set(ings)
            
    possible_allergens = set([ing for allergen, ing_set in d.items() for ing in ing_set])
    
    print('part 1 is ' + str(sum([1 for ing in all_ings if ing not in possible_allergens])))
    
    part2_d = {}
    to_pop = set()
    
    while len(part2_d) < len(d):
        for allergen, ings in d.items():
            if len(ings.difference(to_pop)) == 1:
                part2_d[allergen] = ings.difference(to_pop)
                to_pop = to_pop.union(set(ings))
                
    ordered_p2_dict = collections.OrderedDict(sorted(part2_d.items()))
    
    p2_string = ''
    for ing in ordered_p2_dict.values():
        p2_string = p2_string + max(ing) + ','
    
    print('part 2 is ' + p2_string[:-1])
    
    