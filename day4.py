import numpy as np
import re

with open('2020/day4input.txt', 'r') as file:

    all_passports = []
    passport = []
    for line in file:
        input = line.split()
        if input != []:
            passport.extend(input)
        else:
            all_passports.append(passport)
            passport = []

    valid_counter = 0
    for passport in all_passports:
        counter = 0
        for id in passport:
            if 'cid' != id[:3]:
                counter += 1
        if counter == 7:
            valid_counter += 1
    
    print(valid_counter)
    
    valid_counter = 0
    for passport in all_passports:
        counter = 0
        for id in passport:
            left = id[:3]
            right = id[4:]
            if 'byr' == left:
                if int(right) in range(1920,2003):
                    counter+=1
            elif 'iyr' == left:
                if int(right) in range(2010,2021):
                    counter+=1
            elif 'eyr' == left:
                if int(right) in range(2020,2031):
                    counter+=1
            elif 'pid' == left:
                if len(right) == 9 and right.isdigit():
                    counter+=1
            elif 'hcl' == left:
                if re.match(r'#[a-f0-9]{6}', right):
                    counter+=1
            elif 'ecl' == left:
                if right in ['amb','blu','brn','gry','grn','hzl','oth']:
                    counter+=1
            elif 'hgt' == left:
                if right[-2:] == 'cm':
                    if int(right[:len(right)-2]) in range(150, 194):
                        counter+=1
                elif right[-2:] == 'in':
                    if int(right[:len(right)-2]) in range(59, 77): 
                        counter +=1
        if counter == 7:
            valid_counter += 1
    
    print(valid_counter)
