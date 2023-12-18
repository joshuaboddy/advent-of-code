import numpy as np

def polygon_area(x,y):
        correction = x[-1] * y[0] - y[-1]* x[0]
        main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
        return 0.5*np.abs(main_area + correction)

f = open("input.txt", "r")

vertices = [0]
part1 = False
dirs = {"R": 1+0j, "L": -1+0j, "U": 0+1j, "D": 0-1j} if part1 else {'0': 1+0j, '1': 0-1j, '2': -1+0j, '3': 0+1j}
latest = 0
points_on_boundary = 0

for line in f.readlines():

    line = line.strip()
    if part1:
        d = line[0]
        a = int(line[2:4])
    else:
        d = line[-2]
        a = int(line[-7:-2], 16)
        
    latest += dirs[d] * a
    points_on_boundary += a
    vertices.append(latest)

area = polygon_area(np.array([x.real for x in vertices]), np.array([y.imag for y in vertices]))

# shoelace 
print(area + 1 + points_on_boundary / 2)


