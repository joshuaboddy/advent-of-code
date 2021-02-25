with open('2020/day2input.txt', 'r') as file:
    
    input = [line.strip() for line in file]
   
    parsed_data = [word.replace(':', '-').replace(' ','-').split('-') for word in input]
    
    part_1_counter = 0
    for list in parsed_data:
        letter_freq = list[4].count(list[2])
        if (letter_freq <= int(list[1])) & (letter_freq >= int(list[0])):
            part_1_counter += 1
    
    print(part_1_counter)
    
    part_2_counter = 0
    for list in parsed_data:
        if (list[4][int(list[0])-1] == list[2]) & (list[4][int(list[1])-1] != list[2]):
            part_2_counter += 1
        elif (list[4][int(list[0])-1] != list[2]) & (list[4][int(list[1])-1] == list[2]):
            part_2_counter += 1
    
    print(part_2_counter)