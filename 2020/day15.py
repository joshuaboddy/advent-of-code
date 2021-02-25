import time 

start_time = time.time()

input = [16,12,1,0,15,7,11]

d={}
for enum, val in enumerate(input):
    d[val] = [enum+1]
    
lookup = input[-1]
counter = len(input)

while counter < 30000000:
    if lookup in d.keys():
        if len(d[lookup]) == 1:
            lookup = 0
            d[lookup] = [max(d[lookup]), counter+1] 
        elif len(d[lookup]) > 1:
            lookup = counter - min(d[lookup])
            if lookup in d.keys():
                    d[lookup] = [max(d[lookup]), counter+1]
            else:
                d[lookup] = [counter+1]
            
        counter+=1
print(lookup)

print(time.time() - start_time)
