from player import Player
from hand import Hand 
import sys
sys.path.append('../')
from deck import Deck
from card import Card

def initialize():
	print('Welcome to Blackjack!')

def dealInitialCards(playersList):
	for player in playersList:
		player.hitMe()
		player.hitMe()

def drawCards(playersList):
	for player in playersList:
		while True:
			player.displayHand()
			player.displaySum()
			yesno = input('Do you want another card? Yes or No')
			if yesno == 'Yes':
				player.hitMe()
				print()
				if player.isBust():
					print(player.getName() + ' is a bust!')
					player.displayHand()
					player.displaySum()
					print()
					break
			elif yesno == 'No':
				print()
				break

def winner(playersList):
	winnerDict = {}
	for player in playersList:
		if not player.isBust():
			winnerDict[player.getName()] = player.getSum()
	if winnerDict:
		winningScore = max(winnerDict.values())
		winningList = [names for names, score in winnerDict.items() if score == winningScore]
		if len(winningList) == 1:
			print(winningList[0] + ' is the winner!')
			print()
			print('Thanks for playing!')
		else:
			print(winningList, end= ' ')
			print('have tied!')
			print()
			print('Thanks for playing!')
	else:
		print('Everyone Busted! No Winner. Gameover!')

def main():
	initialize()
	n = int(input('How many players are playing?'))
	playersList = []
	namesList = []
	for x in range(1, n+1):
		playername = input('What is the name of Player ' + str(x) + '?')
		namesList.append(playername)
	while True:
		deck = Deck()
		for name in namesList:	
			playersList.append(Player(name, deck))
		dealInitialCards(playersList)
		drawCards(playersList)
		winner(playersList)
		while True:
			yesno = input('Would you like to play again? Yes or No')
			if yesno == 'Yes':
				#Resetting the Player objects but keeping the same player names
				del playersList[:]
				break
			elif yesno == 'No':
				return

if __name__ == '__main__':
	main()