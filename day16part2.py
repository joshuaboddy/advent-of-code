import pandas as pd

#Input parsing and setting up variables
with open('day16myticket.txt', 'r') as myticket_file:
    
    my_ticket = [line.split(',') for line in myticket_file][0]

with open('day16instructions.txt', 'r') as file:
        
    new_input = [rng.split('-') for line in file for rng in line.strip().replace(' or ', ':').split(':')]
    
    set_of_ranges=set()
    range_per_id = {}

    for i in range(len(new_input)-2):
        if i % 3 == 0:
            rng1 = set([i for i in range(int(new_input[i+1][0]), int(new_input[i+1][1])+1)])
            rng2 = set([i for i in range(int(new_input[i+2][0]), int(new_input[i+2][1])+1)])
            rngs = rng1.union(rng2)
            range_per_id[new_input[i][0]] = rngs
            
            set_of_ranges = set_of_ranges.union(rngs)
        
with open('day16nearbytickets.txt', 'r') as nearby_file:
    
    nearby = pd.DataFrame([line.strip().split(',') for line in nearby_file]).astype(int)
  
#Calculations
part1 = nearby[~nearby.isin(set_of_ranges)].sum().sum()

print(part1)

valid = nearby.loc[nearby.isin(set_of_ranges).all(axis=1)]

valid_rows_per_id = {}

for key, rng in range_per_id.items():
    bool_valid = valid.isin(rng).all(axis=0)
    valid_for_key = list(bool_valid[bool_valid].index)
    valid_rows_per_id[key] = valid_for_key
    
to_pop = []
length = 1
while length < len(valid_rows_per_id):
    for key, valid_rows in valid_rows_per_id.items():
        if len(valid_rows) == length:
            unique_row = set(valid_rows).difference(to_pop) 
            valid_rows_per_id[key] = set(unique_row)
            to_pop = set(valid_rows)
            length +=1 

part_2 = 1
for key, row in valid_rows_per_id.items():
    if key.startswith('departure'):
        part_2*=int(my_ticket[max(row)])
        
print(part_2)
            
    
                

        
  