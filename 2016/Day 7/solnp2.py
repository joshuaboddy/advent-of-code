import re

f = open('input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

total_tls_p2 = 0

for line in lines:

    #parse
    letters = re.findall('[a-zA-Z]+', line)
    outside = letters[::2]
    inside = letters[1::2]
    aba_list=[]
    tls=0
    

    for o in outside:
        for j in range(len(o)):
            aba = o[j:j+3]
            if len(aba)==3:
                if aba[0] == aba[2] and aba[0] != aba[1]:
                    aba_list.append(aba)

    for i in inside:
        for j in range(len(i)):
            bab = i[j:j+3]
            if len(bab)==3:
                if bab[0] == bab[2] and bab[0] != bab[1]:
                    for aba in aba_list:
                        if aba[0]==bab[1] and aba[1]==bab[0]:
                            tls=1

    
    total_tls_p2 = total_tls_p2 + tls
print(total_tls_p2)