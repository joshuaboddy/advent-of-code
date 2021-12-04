import pandas as pd
import numpy as np

def bingo(df):
    
    marked = df == 'x'
    
    column_winner = (marked.sum(axis=0) == len(df)).any()
    row_winner = (marked.sum(axis=1) == len(df)).any()
    diag_winner = False #(np.diag(marked).sum() == len(df)) | (np.diag(np.fliplr(marked)).sum() == len(df))

    return (column_winner | row_winner | diag_winner)


def parse():
    
    f = open('input.txt')
    raw = f.readlines()
    f.close()
    
    lines = list(raw)
    lines = lines + ['\n']
    
    numbers_drawn = [int(x) for x in lines[0].strip().split(',')]
    
    bingo_cards = []
    current_card = pd.DataFrame()
    
    for line in lines[2:]:
        
        line = line.strip()
        
        if line != '':
            current_card = current_card.append(pd.Series([int(x) for x in line.split()]),
                                               ignore_index=True)
        else:
            bingo_cards.extend([current_card])
            current_card = pd.DataFrame()
    
    return numbers_drawn, bingo_cards


def part1():
    
    numbers_drawn, bingo_cards = parse()

    for draw in numbers_drawn:
            for card_num, card in enumerate(bingo_cards):
                card = card.replace(draw, 'x')
                bingo_cards[card_num]= card
                if bingo(card):
                    return card.replace('x',0).to_numpy().sum() * draw


def part2():
    
    numbers_drawn, bingo_cards = parse()
    
    done = []
    if len(done) != len(bingo_cards):
        for draw in numbers_drawn:
            for card_num, card in enumerate(bingo_cards):
                if card_num not in done:
                    card = card.replace(draw, 'x')
                    bingo_cards[card_num]= card
                    if bingo(card):
                        done = done + [card_num]
                        latest_result = card.replace('x',0).to_numpy().sum() * draw

    return latest_result

print(part1())
print(part2())