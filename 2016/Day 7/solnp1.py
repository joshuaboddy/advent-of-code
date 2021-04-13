import re

f = open('input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

total_tls_p1 = 0

for line in lines:

    #parse
    letters = re.findall('[a-zA-Z]+', line)
    outside = letters[::2]
    inside = letters[1::2]
    tls=-1
    
    for i in inside:
        for j in range(len(i)):
            abba = i[j:j+4]
            if len(abba)==4:
                if abba[0] == abba[3] and abba[1] == abba[2] and abba[0] != abba[1]:
                    tls=0
    
    if tls==-1:
        for o in outside:
            for j in range(len(o)):
                abba = o[j:j+4]
                if len(abba)==4:
                    if abba[0] == abba[3] and abba[1] == abba[2] and abba[0] != abba[1]:
                        tls=1
                        break
                    
    if tls==-1:
        tls=0
        
    total_tls_p1 = total_tls_p1 + tls
print(total_tls_p1)