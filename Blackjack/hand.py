import sys
sys.path.append('../')
from card import Card

class Hand():
	facecards = ['J','Q','K']

	def __init__(self):
		self._cards = []
		self._sum = 0
		self._bust = False
		self._hasAce = False
		self._aceCount = 0

	def display(self):
		for x in self._cards:
			print(x)

	def getSum(self):
		self.updateSum()
		return self._sum

	def isBust(self):
		return self._bust


	def updateSum(self):
#Every time we call this function we are recalculating the sum so sum and acecount must reset too
		self._sum = 0
		self._aceCount = 0

		for card in self._cards:
			cardname = card.getName()

			if cardname in Hand.facecards:
				self._sum += 10
			elif cardname == 'A':
				self._hasAce = True
				self._aceCount += 1
				self._sum += 11
			else:
				self._sum += int(cardname)
		if self._hasAce and self._sum > 21:
			self._subtractAce()
		if self._sum > 21:
			self._bust = True

#Accounting for Ace's value of both 1 and 11
#Subtracting 10 from the sum for every ace in the hand until the sum is less than or equal to 21
	def _subtractAce(self):
		for x in range (0, self._aceCount):
			self._sum -= 10
			if self._sum <= 21:
				break

	def addToHand(self, card):
		self._cards.append(card)
