import pandas as pd
import numpy as np

f = open('day20testinput.txt')
raw = f.readlines()
f.close()

d = {}

lines = list(raw)

i = 0

for line in lines:
    line = line.strip()
    if 'Tile' in line:
        i = int(line.replace('Tile ','').replace(':',''))
        d[i] = []
    elif line != '':
        d[i] = d[i] + [line]
        
coords = {}

for key, tile in d.items():
    
    df = pd.DataFrame(tile)[0].str.split('', expand=True)

    df = df.shift(-1, axis=1).drop(columns=[10,11])
    trans = df.T
    flipped = df.iloc[::-1]
    flipped_trans = flipped.T 
    
    # if key == 2473:
    #     print(df)
    #     print(trans)
    #     print(flipped)
    #     print(flipped_trans)
    
    for n, ob in enumerate([df, trans, flipped, flipped_trans]):
        key=str(key)
        coords[key+"_"+str(n)] = [(x, ob.columns[y]) for x, y in zip(*np.where(ob.values == '#'))]
        coords[key+"_"+str(n+4)] = [(9-x, ob.columns[y]) for x, y in zip(*np.where(ob.values == '#'))]

# borders = {}
# for tile, coord in coords.items():
#     for c in coord:
#         if 0 in c or 9 in c:
#             borders[tile] = borders.get(tile, []) + [c]

# def do_tiles_match(tile1, tile2):
        
#     tops = [x[0] for x in tile1 if x[1] == 0]
#     bottoms = [x[0] for x in tile1 if x[1] == 9]
#     lefts = [x[1] for x in tile1 if x[0] == 0]
#     rights = [x[1] for x in tile1 if x[0] == 9]
    
#     other_tops = [x[0] for x in tile2 if x[1] == 0]
#     other_bottoms = [x[0] for x in tile2 if x[1] == 9]
#     other_lefts = [x[1] for x in tile2 if x[0] == 0]
#     other_rights = [x[1] for x in tile2 if x[0] == 9] 
    
#     top_match = int(set(tops) == set(other_bottoms))
#     left_match = int(set(lefts) == set(other_rights))
#     bottom_match = int(set(bottoms) == set(other_tops))
#     right_match = int(set(rights) == set(other_lefts))
    
#     return [top_match,left_match,bottom_match,right_match]

# matches = {}
# for tile in borders: 
#     for other_tile in borders:
#         if tile[:4] not in other_tile:
#             # if tile == '3079_1' and other_tile == ''
#             if sum(do_tiles_match(borders[tile], borders[other_tile])) >= 1:
#                 matches[tile] = matches.get(tile, []) + [other_tile]
        
            
            
            
            
#     # for i in range(8):
#     #     i = str(i)
#         # borders[tile+"_"+i] = {}
#         # borders[tile+"_"+i]['top'] = []
#         # borders[tile+"_"+i]['bottom'] = []
#         # borders[tile+"_"+i]['left'] = []
#         # borders[tile+"_"+i]['right'] = []
#         # for flip in coords[tile+"_"+i]:
#         #     print(flip)
#             # if flip[1] == 0:
#             #     borders[tile][i]['top'].append(flip)
#             # if flip[1] == 9:
#             #     borders[tile][i]['bottom'].append(flip)
#             # if flip[0] == 0:
#             #     borders[tile][i]['left'].append(flip)
#             # if flip[0] == 9:
#             #     borders[tile][i]['right'].append(flip)


# # matches = {}
# # for tile in borders:
# #     matches[tile] = {}
# #     for i in range(8):
# #         matches[tile][i] = []
# #         for other_tiles in borders:
# #             if other_tiles != tile:
# #                 for j in range(8):
# #                     if len([(9-x[0], x[1]) for x in borders[tile][i]['bottom'] if (9-x[0], x[1]) in borders[other_tiles][j]['top']]) == len(borders[other_tiles][j]['top']):
# #                         if len([(x[0], 9-x[1]) for x in borders[tile][i]['left'] if (x[0],9-x[1]) in borders[other_tiles][j]['left']]) == len(borders[other_tiles][j]['right']):
# #                             matches[tile][i] += [other_tiles]
                                                                
#                     # # elif len([(x[0], 9-x[1]) for x in borders[tile][i] if (9-x[0], x[1]) in borders[other_tiles][j]]) == len(borders[other_tiles][j]):
#                     # #     print(tile, i, other_tiles, j)