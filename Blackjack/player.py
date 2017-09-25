import sys
sys.path.append('../')
from deck import Deck
from hand import Hand 

class Player:
#Two types of players: Player and Dealer
#Deck input should be the same deck for every player
	def __init__(self, name, deck, playertype= 'Player'):
		self._name = name
		self._deck = deck
		self._type = playertype
		self._hand = Hand()

	def hitMe(self):
		card = self._deck.draw()
		self._hand.addToHand(card)
		self._hand.updateSum()

	def getName(self):
		return self._name

	def displayHand(self):
		print(self._name + ' has the following cards:')
		self._hand.display()

	def getSum(self):
		return self._hand.getSum()

	def displaySum(self):
		print(self._name + '\'s sum is ' + str(self.getSum()))

	def isBust(self):
		return self._hand.isBust()

def main():
	deck = Deck()
	player = Player('Rodell', deck)
	player.hitMe()
	player.hitMe()
	player.hitMe()
	player.displayHand()
	player.displaySum()

if __name__ == '__main__':
	main()