import pandas as pd

x = pd.read_csv('input.txt', sep=" ", header=None)

x[0] = x[0].astype(str)
df = x[0].str.split('', expand=True)
df.drop(columns=[0, len(x[0]) + 1], inplace=True)

for col in df.columns:
    df[col] = df[col].astype(int)
    
p1=0
p2=0

def viewing_distance(value, adjacent):
    
    visible = (value > adjacent).cumprod().sum()
    
    if visible < len(adjacent):
        return visible + 1
    else:
        return visible

for rowIndex, row in df.iterrows(): 
    for columnIndex, value in row.items():
        left = df.iloc[rowIndex][:columnIndex-1].iloc[::-1]
        right = df.iloc[rowIndex][columnIndex:]
        down = df[columnIndex].iloc[rowIndex+1:]
        up = df[columnIndex].iloc[:rowIndex].iloc[::-1]
        
        if any([all(value > up), all(value > right), all(value > left), all(value > down)]):
            p1+=1
        
        vd = viewing_distance(value, left) * viewing_distance(value, right) * viewing_distance(value, up) * viewing_distance(value, down) 
        if vd > p2:
            p2 = vd
            
print(p1)
print(p2)