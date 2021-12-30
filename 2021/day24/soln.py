#takes 5-10 mins to run
#idea is iterate through all 'states'/values of z and store the highest model
#number that acheives that value
#then just find the model number with state/value of 0 at the end
import re

def MONAD(n1,n2,n3,w,z):
   
    #the MONAD program reduces to a few simple operations on z
    return int(z/n1) * (25 * ((z%26 + n2) != w) + 1) + (w + n3) * ((z%26 + n2) != w)

f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)

n1s = [int(re.findall('-?\d+', line.strip())[0]) for n, line in enumerate(lines) if (n+1)%18 == 5]
n2s = [int(re.findall('-?\d+', line.strip())[0]) for n, line in enumerate(lines) if (n+1)%18 == 6]
n3s = [int(re.findall('-?\d+', line.strip())[0]) for n, line in enumerate(lines) if (n+1)%18 == 16]

states = {0:''}
i = 0
part1=False

while i < len(n1s):
    new_states = states.copy()
    n1=n1s[i]
    n2=n2s[i]
    n3=n3s[i]
    for state, model_num in states.items():
        if len(model_num) == i:
            for j in range(1,10):
                if part1:
                    z = MONAD(n1,n2,n3,j,state)        
                    prev_max = new_states.get(z,'-1')
                    new_states[z] = str(max(int(model_num + str(j)), 
                                            int(-1 if prev_max == '' else prev_max)))
                else:
                    z = MONAD(n1,n2,n3,10-j,state)                  
                    new_states[z] = model_num + str(10-j)
            
    states = new_states.copy()
    i+=1
    
print(states[0])