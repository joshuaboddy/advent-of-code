import re
import pandas as pd
from collections import Counter
import string

f = open('2016/Day 4/input.txt')
rawInput = f.readlines()
f.close()

lines = list(rawInput)

valid_sum=0

for line in lines:

    #parse
    letters = re.findall('[a-zA-Z]+', line)
    sector_id = re.findall('-?\d+', line)
    sector_id = -int(sector_id[0])

    #part 1
    full_letters_string = ''.join(letters[:len(letters)-1])
    order_to_check = letters[-1]

    letters_and_freq = pd.Series([x for x in full_letters_string]).value_counts()

    full_checkstring = []
    for count in letters_and_freq.drop_duplicates():
        full_checkstring += sorted(letters_and_freq[letters_and_freq==count].index)

    checkstring = ''.join(full_checkstring)[:5]

    if checkstring == order_to_check:
        valid_sum += sector_id

    #part 2    
    shifter = sector_id % 26
    alphabet_dict = dict(zip(string.ascii_lowercase, range(26)))
    alphabet_dict_reversed = dict(zip(range(26), string.ascii_lowercase))

    shifted_string = ''
    for letter in full_letters_string:
        shifted_string += alphabet_dict_reversed[(alphabet_dict[letter] + shifter) % 26]
    if 'northpole' in shifted_string:
        print('part 2 is: ' + str(sector_id))


print('part 1 is: ' + str(valid_sum))
    
