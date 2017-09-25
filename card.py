NAME_ENUM = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUIT_ENUM = ['Spades','Hearts','Clubs','Diamonds']

class Card:

#Value and Suit variable should only be from their respective enum list 
	def __init__(self, name,suit, avaialable=True):
		self._name = name
		self._suit = suit
		self._avaialable = avaialable

	def isAvailable(self):
		return self._avaialable

	def markAvailable(self):
		self._avaialable = True

	def markUnavailable(self):
		self._avaialable = False

	def getName(self):
		return self._name

	def getSuit(self):
		return self._suit

	def __str__(self):
		return self._name + ' of ' + self._suit