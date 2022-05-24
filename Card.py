class Card:
    def __init__(self, rank, suit, value):
        """
        Defines a card object
        :param rank: The rank of the card
        :param suit: The suit of the card
        :param value: The values in terms of blackjack rules
        """
        self.rank = rank
        self.suit = suit
        self.value = value

    def show(self):
        """
        show the card
        """
        print("{} of {} | value: {}".format(self.rank, self.suit, self.value))

