f = open('input.txt')
data = [int(x) for x in f.read().strip().split(',')]
f.close()

initial_counter = {}
for i in range(9):
    initial_counter[i] = data.count(i)
    
def fish_count(days, counter):

    for day in range(days):
        
        previous_counter = counter.copy()
        
        for key,value in counter.items():
            counter[key] = previous_counter[(key+1) % 9] + (key==6) * previous_counter[0]

    return sum(counter.values())

print(fish_count(80, initial_counter.copy()))
print(fish_count(256, initial_counter.copy()))
