import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.game = CardGame()
        self.card = Card("Spades", 3)
        self.card1 = Card("Spades",1)
        self.card2 = Card("Diamonds", 10)
        self.card3 = Card("Diamonds", 7)
        self.cards = [11,2,8,3]

    def test_check_for_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 24", self.game.cards_total(self.cards))