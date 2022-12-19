import re
raw = open('input.txt').readlines()

monkeys = {}
inspection_count = {}
modder = 1
part = 1
rounds = 20 if part == 1 else 10000

for line in raw:
    line = line.strip()
    if line.startswith("Monkey"):
        current_monkey = line[:-1]
    
    elif line.startswith("Starting items"):
        items = re.findall('[0-9]+', line)
        monkeys[current_monkey] = items
        
    elif line.startswith("Test"):
        modder = modder * int(re.findall('[0-9]+', line)[0])
        

for r in range(rounds):
    for line in raw:
        line = line.strip()
        if line.startswith("Monkey"):
            current_monkey = line[:-1]
        
        elif line.startswith("Operation"):
            worry_levels = []
            for item in monkeys[current_monkey]:        
                dyn = re.findall('[0-9]+', line.replace("old", str(item)))
                dyn = [int(x) for x in dyn]
                if "*" in line:
                    worry_level = (dyn[0] * dyn[1]) % modder if part == 2 else dyn[0] * dyn[1]
                else:
                    worry_level = (dyn[0] + dyn[1]) % modder if part == 2 else dyn[0] + dyn[1]
                worry_levels.append(worry_level)
                
            bored_worry_levels = [int(x / 3) if part == 1 else x for x in worry_levels]
             
        elif line.startswith("Test"):
            divide_by = int(re.findall('[0-9]+', line)[0])
            
            bools = [bwl % divide_by == 0 for bwl in bored_worry_levels]
            
        elif line.startswith("If true"):
            true_monkey = f"Monkey {re.findall('[0-9]+', line)[0]}"
            
        elif line.startswith("If false"):
            false_monkey = f"Monkey {re.findall('[0-9]+', line)[0]}"
            
        elif line == "":
            for idx, b in enumerate(bools):
                inspection_count[current_monkey] = inspection_count.get(current_monkey, 0) + len(monkeys[current_monkey])
                monkeys[current_monkey] = []
                if b:
                    monkeys[true_monkey] = monkeys.get(true_monkey, []) + [bored_worry_levels[idx]]
                else:
                    monkeys[false_monkey] = monkeys.get(false_monkey, []) + [bored_worry_levels[idx]]
                    
                    
most_inspected = sorted(inspection_count.values())[-2:]
print(most_inspected[0] * most_inspected[1])