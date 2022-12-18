def loop_over_dirs(dirs, dir_path, line):
    
    for path in dir_path:
        if path == "/":
            try:
                subdir = dirs[path]
            except:
                subdir = dirs
        else:
            subdir = subdir[path]
            
        if line.split()[0].isnumeric():
            subdir["d_size"] = subdir.get("d_size", 0) + int(line.split()[0])
            
    return subdir
    
    
def get_dirs_and_sizes():
    
    raw = open('input.txt').readlines()

    dir_path = []
    dirs = dict()
    subdir = dirs
    
    for line in raw:
        line = line.strip()
        
        if line.startswith('$ cd'):
            d = line[5:]
            dir_path.append(d)
            if d == "..":
                dir_path.pop()
                dir_path.pop()
                
        if line.startswith("dir"):
            subdir[line[4:]] = {}
        
        subdir = loop_over_dirs(dirs, dir_path, line)
        
    return dirs
             

part1 = 0
dirs = get_dirs_and_sizes()
part2 = dirs["d_size"]

unused_space = 70000000 - dirs["d_size"] 
space_needed = 30000000 - unused_space


def part1_and_2(d):
    global part1
    global part2

    for k, v in d.items():
        if isinstance(v, dict):
            part1_and_2(v)
        else:
            if v < 100000:
                part1 = part1 + v
            if v > space_needed and v < part2:
                part2 = v
            
            
part1_and_2(dirs)

print(part1)
print(part2)

