import unittest
from playing_card import PlayingCard, Deck, Hand

class TestPlayingCard(unittest.TestCase):
    def test_valid_card(self):
        card = PlayingCard("A", "Hearts")
        self.assertEqual(str(card), "A of Hearts")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            PlayingCard("1", "Hearts")

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard("A", "Stars")

    def test_equality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("10", "Diamonds")
        card3 = PlayingCard("9", "Clubs")
        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)


class TestDeck(unittest.TestCase):
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)  # Standard deck size
        self.assertEqual(str(deck.cards[0]), "2 of Hearts")  # First card

    def test_shuffle(self):
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)  # Check if deck order changed

    def test_draw_cards(self):
        deck = Deck()
        cards_drawn = deck.draw(5)
        self.assertEqual(len(cards_drawn), 5)
        self.assertEqual(len(deck), 47)  # 52 - 5 cards drawn

    def test_draw_too_many_cards(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.draw(53)  # Exceeds deck size


class TestHand(unittest.TestCase):
    def test_draw_random_card(self):
        deck = Deck()
        hand = Hand()
        hand.draw_random_card(deck)
        self.assertEqual(len(hand), 1)
        self.assertEqual(len(deck), 51)

    def test_view_cards(self):
        deck = Deck()
        hand = Hand()
        hand.draw_random_card(deck)
        self.assertEqual(len(hand.view_cards()), 1)
        self.assertIn(hand.view_cards()[0], [str(card) for card in deck.cards + hand.cards])

    def test_hand_length(self):
        hand = Hand()
        self.assertEqual(len(hand), 0)
        deck = Deck()
        hand.draw_random_card(deck)
        self.assertEqual(len(hand), 1)


if __name__ == "__main__":
    unittest.main()
