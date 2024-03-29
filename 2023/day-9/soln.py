import re 

f = open("input.txt", "r")

sum_of_next_values = 0
part1 = False

for line in f.readlines():
    history = [int(string_number) for string_number in re.findall(r'-?\d+', line)]
   
    if not part1:
        history = history[::-1]
        
    next_value = 0     
    while any([x != 0 for x in history]):
        next_value += history[-1] 
        history = [history[i+1] - history[i] for i in range(len(history) - 1)]

    sum_of_next_values += next_value
    
print(sum_of_next_values)