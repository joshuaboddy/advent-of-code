from itertools import chain
import time

start_time = time.time()

class Cup:
    def __init__(self, value):
        self.value = value
        self.prev  = None  
        self.next  = None  

input = '418976235'

vals = [int(char) for char in input]

cups = {}
values = chain(vals[1:], range(10, 1000001))

#set first cups
first = Cup(vals[0])
cups[first.value] = first
prev = first

#create cups linked list
for value in values:

    cup = Cup(value)
    cup.prev = prev
    cup.prev.next = cup
    prev = cup
    cups[cup.value] = cup

#join up ends/beginnings
cup.next = first
first.prev = cup

#lets play
for move in range(10000001):
    
    #use cups as linked list, play game
    pick1 = first.next
    pick2 = pick1.next
    pick3 = pick2.next
    
    picks = (pick1, pick2, pick3)
    
    first.next = pick3.next
    pick3.next.prev = first
    
    #find dest
    dest = Cup(0)
    
    i=1
    while first.value - i in (pick1.value, pick2.value, pick3.value):
        i+=1
    if first.value - i == 0:
        dest = cups[1000000]
    else:
        dest = cups[first.value - i]

    #connect dest
    dest.next.prev = pick3
    pick3.next = dest.next
    dest.next = pick1
    pick1.prev = dest
    
    #next
    first = first.next

print(cups[1].next.value * cups[1].next.next.value)

print(time.time() - start_time, "seconds")