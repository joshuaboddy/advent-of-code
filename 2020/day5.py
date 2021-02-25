import numpy as np

with open('day5input.txt', 'r') as file:
    
    ans = []

    for input in file:
        forward_rows = [0,127]
        side_columns = 8
        
        forward_id = input[:7]
        side_id = input[7:]
        
        forwards_rows = [0,128]
        for x in forward_id:
            if x == 'B':
                forward_rows = [int((forward_rows[0]+forward_rows[1])/2)+1, forward_rows[1]]
            else:
                forward_rows = [forward_rows[0], int((forward_rows[0]+forward_rows[1])/2)]
        row = np.mean(forward_rows)
        
        side_columns = [0,7]
        for y in side_id:
            if y == 'R':
                side_columns = [int((side_columns[0]+side_columns[1])/2)+1, side_columns[1]]
            else:
                side_columns = [side_columns[0], int((side_columns[0]+side_columns[1])/2)]
        column = np.mean(side_columns)
        
        ans.append(row*8 + column)
    print(max(ans))
    print(sorted(ans))