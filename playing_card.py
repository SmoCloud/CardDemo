import random

class PlayingCard:
    """A playing card class"""
    
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        if not isinstance(other, PlayingCard):
            return False
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    """A deck of playing cards consisting of PlayingCard objects"""

    def __init__(self):
        self.cards = [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]

    def shuffle(self):
        """Shuffle the deck of cards"""
        random.shuffle(self.cards)

    def draw(self, num=1):
        """Draw a number of cards from the deck"""
        if num > len(self.cards):
            raise ValueError("Not enough cards in the deck to draw")
        drawn_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return drawn_cards

    def __len__(self):
        """Return the number of cards remaining in the deck"""
        return len(self.cards)

class Hand:
    """A hand of playing cards"""

    def __init__(self):
        self.cards = []

    def draw_random_card(self, deck):
        """Draw a random card from the deck"""
        if len(deck) == 0:
            raise ValueError("No cards left in the deck to draw")
        random_card = random.choice(deck.cards)
        deck.cards.remove(random_card)
        self.cards.append(random_card)

    def view_cards(self):
        """View all the cards in the hand"""
        return [str(card) for card in self.cards]

    def __len__(self):
        """Return the number of cards in the hand"""
        return len(self.cards)

def main():
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    hand.draw_random_card(deck)  # Draw a random card from the deck
    hand.draw_random_card(deck)  # Draw another random card

    print(f"Cards in hand: {hand.view_cards()}")
    print(f"Number of cards in hand: {len(hand)}")
    print(f"Number of cards left in deck: {len(deck)}")

if __name__ == '__main__':
    main()
