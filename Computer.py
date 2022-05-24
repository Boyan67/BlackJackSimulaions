from Hand import Hand


class Computer:
    def __init__(self):
        """
        Creates a computer object to play as the dealer
        """
        self.hand = Hand()

    def reset_hand(self):
        """
        Resets the dealer's hand
        """
        self.hand = Hand()
