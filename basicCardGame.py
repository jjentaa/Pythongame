'''Only the basic for card game only sending the card for player'''
import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def displayCard(self):
        print(f"{self.number}{self.suit}")

class Deck:
    def __init__(self):
        self.suit = ["♠","♥","♦","♣"]
        self.number = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.cards =[]
        for i in self.number:
            for j in self.suit:
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def giveCard(self):
        return self.cards.pop(0)

class Player:
    def __init__(self, name):
        self.name = name
        self.inHand = []

    def getCard(self, card):
        self.inHand.append(card)

    def showCardInHand(self):
        for a in self.inHand:
            a.displayCard()

#instantiate a deck
deck = Deck()

#insantiate player
n = int(input("Enter the number of player in the game :"))
playerList = []
for a in range(n):
    name = input(f"Enter Player{a+1}'s name :")
    playerList.append(Player(name))

#Give and show 2 cards for every players
for p in playerList:
    p.getCard(deck.giveCard())
    p.getCard(deck.giveCard())
    print(f"This is {p.name}'s cards :")
    p.showCardInHand()
