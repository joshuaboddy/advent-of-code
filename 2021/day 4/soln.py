import pandas as pd
import numpy as np

def parse():
    
    f = open('input.txt')
    raw = f.readlines()
    f.close()
    
    lines = list(raw)
    lines = lines + ['\n']
    
    numbers_drawn = [int(x) for x in lines[0].strip().split(',')]
   
    bingo_cards = pd.DataFrame([line.strip().split() for line in lines[2:] if line != '\n']).astype(int)
    
    return numbers_drawn, bingo_cards

def bingo(df):
    
    marked = df == 'x'
    
    column_winner = (marked.groupby(marked.index // 5).sum() == 5).any(axis=1)
    row_winner = (marked.sum(axis=1) == 5).groupby(marked.index // 5).any()
    
    return (column_winner | row_winner)

def answer(numbers_drawn, bingo_cards, part):
    
    card_rows = len(bingo_cards)
    
    for draw in numbers_drawn:
        bingo_cards = bingo_cards.replace(draw, 'x')
        is_bingo = bingo(bingo_cards)
        
        if is_bingo.any():
            
            if part == 'part1':
                if len(bingo_cards)==card_rows:
                    idx = is_bingo[is_bingo].idxmax()
                    return bingo_cards.iloc[idx*5: (idx+1)*5].replace('x', 0).to_numpy().sum() * draw
            
            elif part == 'part2':
                if len(bingo_cards)==5:
                    return bingo_cards.replace('x', 0).to_numpy().sum() * draw
                else:
                    idxs = [y for x in is_bingo[is_bingo].index for y in range(x*5, (x+1)*5)]
                    bingo_cards = bingo_cards[~bingo_cards.index.isin(idxs)]

            
numbers_drawn, bingo_cards = parse()
print(answer(numbers_drawn, bingo_cards, 'part1'))
print(answer(numbers_drawn, bingo_cards, 'part2'))
