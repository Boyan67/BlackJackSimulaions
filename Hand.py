class Hand:
    def __init__(self):
        """
        Creates a hand with the following parameters:
            cards - array of cards in the hand
            total - the current total of the hand
            bust - True or False. If the hand is bust or not
            ace_count - number of aces in the hand
            already_split - True or False. If the hand has already been split once
            blackjack - True or False. If the hand has blackjack
        """
        self.cards = []
        self.total = 0
        self.bust = False
        self.ace_count = 0
        self.already_split = False
        self.bet = 0
        self.blackjack = False

    def check_blackjack(self):
        """
        Checks if the hand has a blackjack
        """
        if self.total == 21:
            self.blackjack = True

    def add(self, card):
        """
        Adds a card to the hand, this is mostly useful for the splitting functionality
        :param card: the card to be added
        """
        self.cards.append(card)
        self.total += card.value

    def show_hand(self):
        """
        Shows all the cards in the given hand
        """
        for card in self.cards:
            card.show()

    def show_values(self):
        """
        Show all the values in the hand
        :return: a string of all the values for the cards in this hand
        """
        a = [x.value for x in self.cards]
        return str(a)

    def is_soft(self):
        """
        Checks if it is a soft hand or a hard hand
        :return: True or False
        """
        count = 0
        for x in self.cards:
            if x.value == 11:
                count += 1
        if count == 1:
            return True
        elif count > 1:
            return False

    def draw(self, deck):
        """
        Draws a card into the hand
        :param deck: the deck to draw from
        :return: the drawn card
        """
        drawn_card = deck.draw_card()
        self.cards.append(drawn_card)
        if drawn_card.value == 11:
            self.ace_count += 1
        if self.total + drawn_card.value > 21 and self.ace_count > 0:
            self.ace_count -= 1
            self.total -= 10
            self.total += drawn_card.value
        elif (self.total + drawn_card.value) > 21 and self.ace_count == 0:
            self.total += drawn_card.value
            self.bust = True
        else:
            self.total += drawn_card.value
        self.check_blackjack()
        return drawn_card

    def hit(self, deck):
        """
        Simply draws a card when hitting nothing else
        :param deck: the deck to draw a card from
        :return: the drawn card
        """
        return self.draw(deck)

    def split(self, deck):
        """
        Handles the splitting functionality: creates two hands from the original hand and draws an extra card
        :param deck: the deck to drawn from
        :return: the new hand produced from splitting
        """
        a = self.cards.pop()
        self.total -= a.value
        if a.value == 11:
            self.total += 10
        self.draw(deck)
        self.check_blackjack()
        new_hand = Hand()
        new_hand.add(a)
        new_hand.draw(deck)
        new_hand.check_blackjack()
        return new_hand

    def return_cards(self):
        return self.cards
