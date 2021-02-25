with open("8test.txt") as file:
    
    input = [lines.strip().split() for lines in file]
    
    # lines = list(enumerate(input))

    # line_jumper = 0
    # acc = 0
    # loop_detector = []
    
    # def func(enum, op, jump, line_counter, acc_counter):
    #     while enum not in loop_detector:
    #         if op == 'nop':
    #             line_counter = line_counter+1
    #             acc_counter = acc_counter
    #         if op == 'jmp':
    #             line_counter = line_counter+int(jump)
    #             acc_counter = acc_counter
    #         if op == 'acc':
    #             line_counter = line_counter+1
    #             acc_counter = acc_counter+int(jump)
            
    #         loop_detector.append(enum)
            
    #         return func(lines[line_counter][0], lines[line_counter][1][0], lines[line_counter][1][1], line_counter, acc_counter)
        
    #     else:
    #         print(acc_counter)
      
    # func(lines[line_jumper][0], lines[line_jumper][1][0], lines[line_jumper][1][1], line_jumper, acc)

    # print(lines)
    
    counter = 0
    for i in range(len(input)):
        new_input = []
        for enum, line in enumerate(input):
            
            if line[0] == 'jmp' and counter == enum:
                new_input.append([enum, ['nop', line[1]]])
            elif line[0] == 'nop' and counter == enum:
                new_input.append([enum, ['jmp', line[1]]])
            else:
                new_input.append([enum, line])
        counter += 1
        
        line_jumper = 0
        acc = 0
        loop_detector = []

        def func2(enum, op, jump, line_counter, acc_counter):
            while enum not in loop_detector:
                if op == 'nop':
                    line_counter = line_counter+1
                    acc_counter = acc_counter
                if op == 'jmp':
                    line_counter = line_counter+int(jump)
                    acc_counter = acc_counter
                if op == 'acc':
                    line_counter = line_counter+1
                    acc_counter = acc_counter+int(jump)
                
                loop_detector.append(enum)
                try:
                    return func2(new_input[line_counter][0], new_input[line_counter][1][0], new_input[line_counter][1][1], line_counter, acc_counter)
                except:
                    print(acc_counter)
            
                
          
    
        func2(new_input[line_jumper][0], new_input[line_jumper][1][0], new_input[line_jumper][1][1], line_jumper, acc)
        
        
            
    
    # def func(enum, op, jump, line_counter, acc_counter):
    #     while enum not in loop_detector:
    #         if op == 'nop':
    #             line_counter = line_counter+1
    #             acc_counter = acc_counter
    #         if op == 'jmp':
    #             line_counter = line_counter+int(jump)
    #             acc_counter = acc_counter
    #         if op == 'acc':
    #             line_counter = line_counter+1
    #             acc_counter = acc_counter+int(jump)
    #         loop_detector.append(enum)
            
            
    #         return func(lines[line_counter][0], lines[line_counter][1][0], lines[line_counter][1][1], line_counter, acc_counter)
    #     else:
    #         print(acc_counter)
      
    # func(lines[line_jumper][0], lines[line_jumper][1][0], lines[line_jumper][1][1], line_jumper, acc)

