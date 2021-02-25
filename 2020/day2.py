impo

with open('day2input.txt', 'r') as file:
    input = [line.strip() for line in file]
   
    parsed_data = [word.replace(':', '-').replace(' ','-').split('-') for word in input]
    
    df = 
    
    # part_1_counter = 0
    # for list in parsed_data:
    #     counted = list[4].count(list[2])
    #     if (counted <= int(list[1])) & (counted >= int(list[0])):
    #         part_1_counter += 1
    
    # print(part_1_counter)
    
    # part_2_counter = 0
    # for list in parsed_data:
    #     if (list[4][int(list[0])-1] == list[2]) & (list[4][int(list[1])-1] != list[2]):
    #         part_2_counter += 1
    #     elif (list[4][int(list[0])-1] != list[2]) & (list[4][int(list[1])-1] == list[2]):
    #         part_2_counter += 1
    
    # print(part_2_counter)