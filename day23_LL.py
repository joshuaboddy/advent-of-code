from itertools import chain

class Cup:
    def __init__(self, value):
        self.value = value # actual value
        self.prev  = None  # pointer to previous Cup (left)
        self.next  = None  # pointer to next Cup (right)

input = '389125467'

vals = [int(char) for char in input]

def create_list(vals):
    
    cups   = [None] * (10 + 1) 
    values = chain(vals, range(10, 10 + 1))
    
    #initiate
    first = next(values)
    cups[first] = Cup(first)
    first = cups[first]
    prev = first  
    
    for value in vals:
        current = cups[value] = Cup(value)
        current.prev = prev
        prev.next = current
        prev = current
        
    current.next = first
    
    cups = [cup for cup in cups if cup is not None]

    return first, cups

l = create_list(vals)

max_cup = len(l[1]) - 1

current = l[0]

print(current.next.value)

# for move in range(100):
#     pick1 = current.next
#     pick2 = pick1.next
#     pick3 = pick2.next
    
#     picked = (pick1, pick2, pick3)
    
#     current.next = pick3.next
#     pick3.next.prev = current
    
#     dst = 0 
#     if current.value - 1 == 0:
#         dst = max_cup
#     else:
#         i = 1
#         while current.value - i in picked:
#             i+=1
#         dst = current.value - i
        
#     print(pick1.value, pick2.value, pick3.value, dst)
#     pick1.prev = l[1][dst]
#     pick3.next = l[1][dst].next
        
#     l[1][dst].next.prev = pick3
#     l[1][dst].next = pick1
    
#     current = current.next
    