import time 

start_time = time.time()

input = [16,12,1,0,15,7,11]

d={}
for enum, val in enumerate(input):
    d[val] = enum+1
    
lookup = input[-1]
counter = len(input)

while counter < 30000000:
    if lookup not in d.keys():
        new = 0
    else:
         new = counter - d[lookup]
    d[lookup] = counter
    lookup = new
            
    counter+=1
print(lookup)

print(time.time() - start_time)
