x=[288,330] 
y=[-96,-50]

def p1(y):
    
    lowest_odd = min([j for j in range(y[0], y[1]) if j % 2 == 1])

    return int(lowest_odd * (lowest_odd+1) / 2)


def in_target(vel_x, vel_y, min_x, max_x, min_y, max_y):

    pos = (vel_x,vel_y)
    
    if max_x >= pos[0] >= min_x and min_y <= pos[1] <= max_y:
        return 1

    while pos[0] < max_x and pos[1] > min_y:
        vel_x = vel_x - 1
        vel_y = vel_y - 1
        pos = (pos[0] + max(0, vel_x), pos[1] + vel_y)

    
        if max_x >= pos[0] >= min_x and min_y <= pos[1] <= max_y:
            return 1
        
    return 0

p2 = 0
for i in range(max(x)+1):
    for j in range(min(y)-1, -min(y)+1):
        p2 += in_target(i,j,min(x),max(x),min(y),max(y))
        
print(p1(y))    
print(p2)