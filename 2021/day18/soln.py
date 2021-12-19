import re
import math
import itertools

def add(s1, s2):
    
    if s1 != '':

        return '[' + s1 + ',' + s2 + ']'
    
    else:
        return s1+s2

def explode(s):

    fifth_bracket = [(s[:i].count('[') - s[:i].count(']')) == 5 for i in range(len(s))].index(True)
    pair_idx = [num >= fifth_bracket and i.isnumeric() for num, i in enumerate(s)].index(True)
    end_par_idx = s[pair_idx:].index(']')
    
    l, r = s[pair_idx:pair_idx+end_par_idx].split(',')
 
    s_right = s[pair_idx+end_par_idx+1:]
    right_int = re.search('\d+', s_right)
    
    s_left = s[:pair_idx-1]
    left_int = re.search('\d+', s_left[::-1])

    if left_int:
        new_left_int = int(l) + int(left_int.group()[::-1])
        s_left = s_left[::-1].replace(left_int.group(), str(new_left_int)[::-1], 1)[::-1]
    
    if right_int:
        new_right_int = int(r) + int(right_int.group())
        s_right = s_right.replace(right_int.group(), str(new_right_int), 1)
    
    return s_left+'0'+s_right

def split(s):
    
    split_idx = [x for x in re.findall('-?\d+', s) if int(x) > 9]
    if split_idx:
        split = split_idx[0]
        rep = '[' + str(math.floor(int(split)/2))+ ',' + str(math.ceil(int(split)/2)) + ']'
        s = s.replace(split, rep, 1)
        
    return s

def reduce(s):
    
    while any([s[:i].count('[') - s[:i].count(']') == 5 for i in range(len(s))]) or any([int(x) > 9 for x in re.findall('-?\d+', s)]):

        if any([s[:i].count('[') - s[:i].count(']') == 5 for i in range(len(s))]):
            s = explode(s)
       
        elif any([int(x) > 9 for x in re.findall('-?\d+', s)]):
            s = split(s)
            
    return s


def magnitude(s):
    
    while '[' in s:
        
        search_for_inner_brackets = re.search('\[\d+,\d+\]', s)
        
        brackets_to_calculate = search_for_inner_brackets.group()
        l, r = brackets_to_calculate.split(',')
        mag = 3*int(l[1:]) + 2*int(r[:-1])
        s = s.replace(brackets_to_calculate, str(mag))
  
        
    return int(s)


f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)

p1_string=''
snails = []
for line in lines:
    
    snail = line.strip()
    snails.append(snail)
    
    p1_string = add(p1_string, snail)
    p1_string = reduce(p1_string)


max_magnitude = 0
for x in itertools.combinations(snails, 2):
    com1 = add(x[0], x[1])
    max_magnitude = max(max_magnitude, magnitude(reduce(com1)))
    com2 = add(x[1], x[0])
    max_magnitude = max(max_magnitude, magnitude(reduce(com2)))

print(magnitude(p1_string))
print(max_magnitude) 