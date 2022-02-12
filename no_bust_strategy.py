# Strategy from:
# https://wizardofodds.com/games/no-bust-21/
pair_splitting = [['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H'],  # A,A
                  ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # 10,10
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'S', 'Y', 'Y', 'S', 'S'],  # 9,9
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H'],  # 8,8
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H', 'H'],  # 7,7
                  ['H', 'H', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H', 'H'],  # 6,6
                  ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H', 'H'],  # 5,5
                  ['H', 'H', 'H', 'Y', 'Y', 'H', 'H', 'H', 'H', 'H'],  # 4,4
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H'],  # 3,3
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H']]  # 2,2

soft_total = [['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Soft 20
              ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Soft 19
              ['H', 'D', 'D', 'D', 'D', 'S', 'H', 'H', 'H', 'H'],  # Soft 18
              ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 17
              ['H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 16
              ['H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 15
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Soft 14
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]  # Soft 13

hard_total = [['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H'],  # Hard 17
              ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 16
              ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 15
              ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 14
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 13
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 12
              ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],  # Hard 11
              ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H', 'H'],  # Hard 10
              ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Hard 9
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 8
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 7
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 6
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 5
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]  # Hard 4


def no_bust_strategy(hand, up_card, das):
    card1 = hand.cards[0].value
    card2 = hand.cards[1].value

    if hand.total == 21:
        choice = "S"
    elif len(hand.cards) == 2 and card1 == card2:
        choice = pair_splitting[11 - card1][up_card - 2]
    elif hand.ace_count == 1:
        choice = soft_total[10 - (hand.total - 10)][up_card - 2]
    else:
        if hand.total > 17:
            choice = "S"
        else:
            choice = hard_total[17 - hand.total][up_card - 2]

    if hand.already_split and choice == "Y":
        if hand.total > 17:
            choice = "S"
        else:
            choice = hard_total[17 - hand.total][up_card - 2]

    if not das:
        if hand.already_split and choice == "D":
            choice = "H"

    return choice
