from card import *
import random

class Deck:

	def __init__(self):

		self._cards = [Card(name, suit) for name in NAME_ENUM for suit in SUIT_ENUM]
		for x in range(0,50):
			random.shuffle(self._cards)
		self._size = len(self._cards)

	def getSize(self):
		return self._size

	def draw(self):
		if self._size > 0:
			self._size -= 1
			return self._cards.pop()
		else:
			print('Deck is empty!')

	def displayDeck(self):
		for card in self._cards:
			print(card)

def main():
	deck = Deck()
	deck.displayDeck()
	print(deck.draw())

if __name__ == '__main__':
	main()