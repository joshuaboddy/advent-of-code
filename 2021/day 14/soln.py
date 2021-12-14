f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)

# tracker dict has the frequency per double letter
tracker = {}

start_string = lines[0].strip()
for i in range(len(start_string)-1):
    tracker[start_string[i:i+2]] = tracker.get(start_string[i:i+2], 0) + 1

last_two_letters = start_string[-2:]

for _ in range(40):
    
    new_tracker = {}
    
    for line in lines[2:]:
        x, y = line.strip().split(' -> ')
        
        prev_freq = tracker.get(x, 0)
        
        new_tracker[x[0]+y] = new_tracker.get(x[0]+y, 0) + tracker.get(x, 0)
        new_tracker[y+x[1]] = new_tracker.get(y+x[1], 0) + tracker.get(x, 0)
        
        if x == last_two_letters:
            last_two_letters = y + last_two_letters[-1]
    
    tracker = new_tracker.copy()
    
freq_per_letter = {}
for k, v in tracker.items():
    freq_per_letter[k[0]] = freq_per_letter.get(k[0], 0) + v
    
freq_per_letter[last_two_letters[-1]] += 1
    
print(max(freq_per_letter.values()) - min(freq_per_letter.values()))