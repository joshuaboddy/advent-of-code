import pandas as pd

#part 1
data = pd.read_csv('input.txt', dtype=str, header=None)[0].str.split('', expand=True).drop(columns=[0,13]).astype(int)
gamma = (data.sum(axis=0) > len(data)/2).astype(int)
epsilon = 1-gamma

#string -> binary -> decimal
print(int(gamma.astype(str).str.cat(),2) * int(epsilon.astype(str).str.cat(),2))

#part 2
oxygen_data = data.copy()
scrubber_data = data.copy()

for bit in oxygen_data.columns:
    keep = (oxygen_data[bit].sum() >= len(oxygen_data[bit])/2).astype(int)

    if len(oxygen_data) > 1:
        oxygen_data = oxygen_data[oxygen_data[bit] == keep]

for bit in scrubber_data.columns:
    keep = (scrubber_data[bit].sum() < len(scrubber_data[bit])/2).astype(int)

    if len(scrubber_data) > 1:
        scrubber_data = scrubber_data[scrubber_data[bit] == keep]

print(int(oxygen_data.iloc[0].astype(str).str.cat(),2) * int(scrubber_data.iloc[0].astype(str).str.cat(),2))