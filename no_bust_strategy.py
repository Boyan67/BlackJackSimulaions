def no_bust_strategy(hand):
    """
    No bust strategy: Avoid busting at all costs, anything above 11 you simply stand
    :param hand: the player's hand
    :return: the choice of the plater: Hit or Stand
    """
    choice = "S"
    if hand.total > 11:
        choice = "S"
    elif hand.total <= 11:
        choice = "H"
    return choice


def mimic_dealer(hand):
    """
    Mimic the dealer strategy: If the player has less than 17 he hits else he stands, just like the dealer
    :param hand: the player's hand
    :return: the choice the player is going to make: Hit or Stand
    """
    choice = ""
    if hand.total < 17:
        choice = "H"
    elif hand.total >= 17:
        choice = "S"
    return choice
