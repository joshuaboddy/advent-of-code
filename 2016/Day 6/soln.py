import pandas as pd

part1 = ''
part2 = ''

df = pd.read_csv('input.txt', sep=r'\s{0,}', header=None)
df = df.drop(columns=[0,9])

for col in df.columns:
    part1 = part1 + df[col].value_counts().index[0]
    part2 = part2 + df[col].value_counts().index[-1]
    
print(part1)
print(part2)