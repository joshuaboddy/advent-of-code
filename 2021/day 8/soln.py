def reverse_dict(d):
    
    reversed_dict = {}
    
    for k, v in d.items():
        reversed_dict.setdefault(v, []).append(k)
        
    return reversed_dict


segments = {1: 2,
            4: 4,
            7: 3,
            8: 7,
            2: 5,
            3: 5,
            5: 5, 
            9: 6,
            0: 6,
            6: 6}

inv_segments = reverse_dict(segments)

f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)

part1=0
part2=0

for line in lines:
    
    p2_sorted = {}
    
    line = line.strip()
    part1 += sum([len(inv_segments[len(word)]) == 1 for word in line.split()[-4:]])
    
    #get the signals and sort them by their number of segments
    #this means that all of the 'easy' signals are identified first
    #and we can then compare these to our 'hard' signals
    signals = line.split()[0:10]
    signals = sorted(signals, key=lambda signal: len(inv_segments[len(signal)])*len(signal))
    
    for signal in signals:
        if len(signal) not in [5,6]:
            p2_sorted[''.join(sorted(signal))] = inv_segments[len(signal)][0]
            
        #for signals of length 5 we have 2,3,5 as the options
        #2 shares 2 segments with 4, 3 and 5 share 3 segments with 4
        #3 shares 2 segments with 1, 5 shares 1 segment with 1
        elif len(signal) == 5:
            four_signal = reverse_dict(p2_sorted)[4][0]
            one_signal = reverse_dict(p2_sorted)[1][0]
            signal = ''.join(sorted(signal))
            
            if len(set(four_signal).intersection(set(signal))) == 2:
                p2_sorted[signal] = 2
                
            elif len(set(one_signal).intersection(set(signal))) == 2:
                p2_sorted[signal] = 3
            
            else:
                p2_sorted[signal] = 5
    
        #for signals of length 6 we have 0,6,9 as the options
        #0 shares 4 segments with 5, 6 and 9 share 5 segments with 5
        #6 shares 2 segments with 7, 9 shares 3 segments with 7
        elif len(signal) == 6:
            
            five_signal = reverse_dict(p2_sorted)[5][0]
            seven_signal = reverse_dict(p2_sorted)[7][0]
            signal = ''.join(sorted(signal))
            
            if len(set(five_signal).intersection(set(signal))) == 4:
                p2_sorted[signal] = 0
                
            elif len(set(seven_signal).intersection(set(signal))) == 2:
                p2_sorted[signal] = 6
            
            else:
                p2_sorted[signal] = 9
            
            
    part2 += int(''.join([str(p2_sorted[''.join(sorted(word))]) for word in line.split()[-4:]]))

print(part1)
print(part2)