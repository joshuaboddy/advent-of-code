def parse_input(path):
    
    f = open(path)
    raw = f.readlines()
    f.close()
    
    lines = list(raw)
    line_break = lines.index('\n')
        
    image = {}
    image_enhancement = ''
    
    for y_coord, line in enumerate(lines):
        
        line = line.strip()
        
        if y_coord < line_break:
            image_enhancement += line
            
        elif y_coord > line_break:
            for x_coord, x in enumerate(line):
                image[(x_coord, y_coord - line_break - 1)] = x
                
    return image, image_enhancement
            

def enhancement_algorithm(part):
    
    image, image_enhancement = parse_input('input.txt')
    
    iters = 2 if part == 1 else 50
    
    max_x, max_y = map(lambda a: max(a)+2, zip(*image.keys()))
    min_x, min_y = map(lambda a: min(a)-1, zip(*image.keys()))
    
    for enhance in range(iters):
    
        enhanced_image = {}
        
        for x in range(*(min_x - enhance, max_x + enhance)):
            for y in range(*(min_y - enhance, max_y + enhance)):
                coord = (x, y)
                nbr_string = ''
                
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if enhance % 2 == 0:
                            nbr_string += image.get((coord[0] + j, coord[1] + i), image_enhancement[-1])
                        else:
                            nbr_string += image.get((coord[0] + j, coord[1] + i), image_enhancement[0])
                            
                nbr_bin = int(nbr_string.replace('#', '1').replace('.', '0'), 2)
                enhanced_image[coord] = image_enhancement[nbr_bin]
                
        image = enhanced_image.copy()
        
    return list(enhanced_image.values()).count('#')

print(enhancement_algorithm(1))
print(enhancement_algorithm(2))