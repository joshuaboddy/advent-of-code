import pandas as pd

raw = pd.read_csv('input.txt', header=None)
cycles = [20 + 40*i for i in range(6)]

#part 1
signal = pd.DataFrame(raw[0].str.split().explode().reset_index(drop=True))
signal[0] = signal[0].apply(lambda x: int(x) if x.lstrip("-").isdigit() else 0)
signal["lag"] = signal[0].shift(1).fillna(0)
signal["value"] = 1 + signal["lag"].cumsum()
signal["cycle"] = signal.index + 1
signal["strength"] = signal["value"] * signal["cycle"]

print(signal.loc[signal["cycle"].isin(cycles)]["strength"].sum())

# part 2
signal["cyclemod"] = (signal["cycle"] - 1) % 40
signal["is_sprite_overlap"] =  signal["value"].between((signal["cyclemod"] - 1), (signal["cyclemod"] + 1)) 
signal["image"] = "."
signal.loc[signal["is_sprite_overlap"], "image"] = '#'
 
for i in range(6):
    print(''.join(list(signal.iloc[0+40*i:40+40*i]["image"])))