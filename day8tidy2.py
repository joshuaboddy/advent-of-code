with open("day8input.txt") as file:
    
    input = [lines.strip().split() for lines in file]
    
    formatted_input = list(enumerate(input))

    loop_detector = []
    
    def rules(op, jump, line_counter, acc_counter):
            if op == 'nop':
                line_counter = line_counter+1
            if op == 'jmp':
                line_counter = line_counter+int(jump)
            if op == 'acc':
                line_counter = line_counter+1
                acc_counter = acc_counter+int(jump)
                
            return [line_counter, acc_counter]
        
    def part1func(lines, line_counter, acc_counter):
        while line_counter not in loop_detector:
            
            ans = rules(lines[line_counter][1][0], lines[line_counter][1][1], line_counter, acc_counter)
           
            loop_detector.append(line_counter)
            
            return part1func(lines, ans[0], ans[1])     
       
        else:
            return acc_counter
      
    print(part1func(formatted_input, 0, 0))
    
    def part2func(lines, line_counter, acc_counter):
        while line_counter not in loop_detector:
        
            ans = rules(lines[line_counter][1][0], lines[line_counter][1][1], line_counter, acc_counter)
           
            loop_detector.append(line_counter)
                      
            try:
                return part2func(lines, ans[0], ans[1])
            except:
                print(acc_counter)

    for i in range(len(input)):
        new_input = []
        for enum, line in enumerate(input):
            
            if line[0] == 'jmp' and i == enum:
                new_input.append([enum, ['nop', line[1]]])
            elif line[0] == 'nop' and i == enum:
                new_input.append([enum, ['jmp', line[1]]])
            else:
                new_input.append([enum, line])        

        loop_detector = []
        part2func(new_input, 0, 0)
                

