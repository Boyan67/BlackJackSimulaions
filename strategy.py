pair_splitting = [['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],  # A,A
                  ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # 10,10
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'S', 'Y', 'Y', 'S', 'S'],  # 9,9
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],  # 8,8
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H', 'H'],  # 7,7
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H', 'H', 'H'],  # 6,6
                  ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],  # 5,5
                  ['H', 'H', 'H', 'Y', 'Y', 'H', 'H', 'H', 'H', 'H'],  # 4,4
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H', 'H'],  # 3,3
                  ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'H', 'H']]  # 2,2

soft_total = [['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Soft 20
              ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Soft 19
              ['D', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H', 'H'],  # Soft 18
              ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 17
              ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 16
              ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 15
              ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Soft 14
              ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H']]  # Soft 13

hard_total = [['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Hard 17
              ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 16
              ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 15
              ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 14
              ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 13
              ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Hard 12
              ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],  # Hard 11
              ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],  # Hard 10
              ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Hard 9
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 8
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 7
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 6
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Hard 5
              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]  # Hard 4


def pair_deviations(total, up_card, count, card1):
    choice = ""
    if total == 20 and up_card == 5 and count >= 5:
        choice = "Y"
    elif total == 20 and up_card == 6 and count >= 5:
        choice = "Y"
    else:
        choice = pair_splitting[11 - card1][up_card - 2]
    return choice


def soft_deviations(total, up_card, count):
    choice = ""
    if total == 19 and up_card == 4 and count >= 3:
        choice = "D"
    elif total == 19 and up_card == 5 and count >= 1:
        choice = "D"
    elif total == 19 and up_card == 6 and count >= 0:
        choice = "D"
    elif total == 17 and up_card == 2 and count >= 1:
        choice = "D"
    else:
        choice = soft_total[10 - (total - 10)][up_card - 2]
    return choice


def hard_deviations(total, up_card, count):
    choice = ""
    if total > 17:
        choice = "S"
    elif total == 16 and up_card == 9 and count >= 5:
        choice = "S"
    elif total == 16 and up_card == 10 and count >= 0:
        choice = "S"
    elif total == 15 and up_card == 10 and count >= 4:
        choice = "S"
    elif total == 13 and up_card == 2 and count >= -1:
        choice = "S"
    elif total == 13 and up_card == 3 and count >= -2:
        choice = "S"
    elif total == 12 and up_card == 2 and count >= 4:
        choice = "S"
    elif total == 12 and up_card == 3 and count >= 2:
        choice = "S"
    elif total == 12 and up_card == 4 and count >= 0:
        choice = "S"
    elif total == 12 and up_card == 5 and count >= -1:
        choice = "S"
    elif total == 12 and up_card == 6 and count >= -1:
        choice = "S"
    elif total == 11 and up_card == 11 and count >= +1:
        choice = "D"
    elif total == 10 and up_card == 10 and count >= 4:
        choice = "D"
    elif total == 10 and up_card == 11 and count >= 4:
        choice = "D"
    elif total == 9 and up_card == 2 and count >= 1:
        choice = "D"
    elif total == 9 and up_card == 7 and count >= 4:
        choice = "D"
    else:
        choice = hard_total[17 - total][up_card - 2]
    return choice


def basic_strategy(hand, up_card, das, count):
    card1 = hand.cards[0].value
    card2 = hand.cards[1].value

    if hand.total == 21:
        choice = "S"
    elif len(hand.cards) == 2 and card1 == card2:
        choice = pair_deviations(hand.total, up_card, count, card1)
    elif hand.ace_count == 1:
        choice = soft_deviations(hand.total, up_card, count)
    else:
        choice = hard_deviations(hand.total, up_card, count)

    if hand.already_split and choice == "Y":
        if hand.total > 17:
            choice = "S"
        else:
            choice = hard_deviations(hand.total, up_card, count)
    return choice
