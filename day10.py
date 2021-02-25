import pandas as pd

with open('day10input.txt', 'r') as file:
    
    input = [int(line.strip()) for line in file]
    
    df = pd.DataFrame(sorted(input))
    
    one_vs_three = (df - df.shift(1).fillna(0)).append(pd.Series([3]), ignore_index=True).value_counts()
    
    part_1_ans = one_vs_three.product()

    input.append(0)

    dict_count={}
    for num in sorted(input):
        if num == 0:
            dict_count[num] = 1
        else:
            dict_count[num] = dict_count.get(num-1, 0) + dict_count.get(num-2, 0) + dict_count.get(num-3, 0)
        
    print(dict_count[max(input)])        
