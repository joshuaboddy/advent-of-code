f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

def set_strengths(part2):

    hand_strengths = [[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]][::-1]
    
    card_and_strength = {
            card: '0' + str(idx) if idx < 10 else str(idx)
            for idx, card in
            enumerate(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1], 1)
        }
    
    if part2: 
        del card_and_strength['J']
        
    return hand_strengths, card_and_strength


def account_for_jokers_in_hands(hand, hand_strength):
    
    js = hand.count("J")
    if js != 5:
        most_cards = list(hand_strength.keys())[-1]
        hand_strength[most_cards] = min(5, hand_strength[most_cards] + js)
    else:
        hand_strength['J'] = 5
        
    return hand_strength


def get_hands_and_points(lines, hand_strengths, valid_cards, part2):
    
    hands_and_points = {}
    for line in lines:
        hand_and_bet = line.split()
        hand = hand_and_bet[0]
        bet = int(hand_and_bet[1])
        
        hand_strength = {}
        for card in set(hand):
            if card in valid_cards:
                hand_strength[card] = hand.count(card)
                
        hand_strength = dict(sorted(hand_strength.items(), key=lambda item: item[1]))    
        
        if part2:
            hand_strength = account_for_jokers_in_hands(hand, hand_strength)
            
        points = hand_strengths.index(sorted(list(hand_strength.values()), reverse=True))
        
        hands_and_points[points] = hands_and_points.get(points, []) + [(hand, bet)]

    return dict(sorted(hands_and_points.items()))


def hands_and_points_to_winnings(hands_and_points, card_and_strength):
    fully_ordered = []
    for strength, cards in hands_and_points.items():
        high_card_maps = []
        for hand_and_bet in cards:
            hand = hand_and_bet[0]
            high_card_map = ''.join([card_and_strength.get(card, '00') for card in hand])
            high_card_maps.append(high_card_map)
            
        sorted_cards_maps = [card[1] for _, card in sorted(zip(high_card_maps, cards), reverse=False, key=lambda pair: pair[0])]
        fully_ordered.extend(sorted_cards_maps)


    return sum([idx * bet for idx, bet in enumerate(fully_ordered, 1)])


part2 = True
hand_strengths, card_and_strength = set_strengths(part2)
hands_and_points = get_hands_and_points(lines, hand_strengths, card_and_strength.keys(), part2)
winnings = hands_and_points_to_winnings(hands_and_points, card_and_strength)

print(winnings)





