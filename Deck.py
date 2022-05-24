from Card import Card
import random


class Deck:
    def __init__(self, size):
        """
        Creates a new shoe with the number of decks specified
        :param size: how many decks should be used
        """
        self.cards = []
        self.build(size)

    def build(self, size):
        """
        Builds multiple decks
        :param size: number of decks
        """
        for i in range(size):
            self.build_deck()

    def build_deck(self):
        """
        Builds all 52 cards within a single deck
        """
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for r in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                if r.isdigit():
                    val = int(r)
                elif r == "Ace":
                    val = 11
                else:
                    val = 10
                self.cards.append(Card(r, s, val))

    def show(self):
        """
        show all the cards in the deck currently. Mostly for testing
        """
        str_rep = [str(x) for x in self.cards]
        print(str_rep)

    def shuffle(self):
        """
        Shuffles the deck
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draw a card from the top of the deck
        :return: the drawn card
        """
        return self.cards.pop()

    def size(self):
        """
        Returns the current size of the shoe closest to the 0.5 of a deck
        :return: the shoe size
        """
        if len(self.cards) < 52:
            return .5
        else:
            return round(len(self.cards) / 52)
