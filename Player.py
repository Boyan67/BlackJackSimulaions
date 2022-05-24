from Hand import Hand


class Player:
    def __init__(self, name):
        """
        Creates a new player with an inital bankroll of 1000 and an empty hand
        :param name: a name for the player
        """
        self.name = name
        self.hand = Hand()
        self.bank = 10000

    def update_bank(self, amount):
        """
        Updates the player bankroll
        :param amount: how much to add to the bankroll, negative values mean losing money
        """
        self.bank += amount

    def reset_hand(self):
        """
        Get rid of all the cards in the player's hand and create a new empty one
        """
        self.hand = Hand()
