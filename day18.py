def find_nth(string, substring, n):
   
    if (n == 1):
       return string.find(substring)
    else:
       return string.find(substring, find_nth(string, substring, n - 1) + 1)

def find_inner_bracket(string):
    
    lbs = find_nth(string, '(', string.count('(')) + 1
    
    rbs = string[lbs:].find(')')
    
    return string[lbs:lbs+rbs]

def apply_left_to_right(string):
    
    splitter = string.split(' ')
    
    res = int(splitter[0])
    
    iters = int(len(splitter)/2)

    for i in range(iters):
        if splitter[1] == '*':
            res = res * int(splitter[2])
        else:
            res = res + int(splitter[2])
            
        splitter = splitter[3:]
        splitter.insert(0, res)
    
    return res

def apply_add_then_multi(string):
    
    splitter = string.split(' ')
    
    iters = int(len(splitter)/2)
    
    for i in range(iters):
        if '+' in splitter:
            index = splitter.index('+')
            res = int(splitter[index-1]) + int(splitter[index+1])
            
            splitter.pop(index-1)
            splitter.pop(index-1)
            splitter.pop(index-1)
            
            splitter.insert(index-1, res)
            
        else:
            res = int(splitter[0]) * int(splitter[2])
           
            splitter = splitter[3:]
            splitter.insert(0, res)
        
    return splitter[0]
            

def remove_all_brackets(string, part):
    
    for i in range(string.count('(')):
        to_replace = find_inner_bracket(string)
        if part == 'part 1':
            string_with_brackets_removed = string.replace('(' + to_replace + ')', str(apply_left_to_right(to_replace)))
        else:
            string_with_brackets_removed = string.replace('(' + to_replace + ')', str(apply_add_then_multi(to_replace)))
       
        string=string_with_brackets_removed
    
    return string

def calculate_line(string, part):
    
    if part == 'part 1':
        ans = apply_left_to_right(remove_all_brackets(string, part))
    else:
        ans = apply_add_then_multi(remove_all_brackets(string, part))
    return ans


with open('day18input.txt', 'r') as file:
    
    ans = print(sum([calculate_line(line.strip(), 'part 2') for line in file]))

