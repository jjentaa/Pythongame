'''
Blackjack game with 2 player
'''

import random

class Deck:
    def __init__(self):
        self.suit = ["♠","♥","♦","♣"]
        self.number = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.cards =[]
        for i in self.number:
            for j in self.suit:
                self.cards.append([i, j])
        random.shuffle(self.cards)

class GM:
    def __init__(self, cards):
        self.cards = cards 
        
    def giveCard(self):
        return self.cards.pop(0)
    
    def showResult(self, p1, p2):
        print("The result is ...")
        if p1 > 21 and p2 > 21:
            print("All Bust!")
        else:
            if p1 == p2:
                print("Draw")
            elif (p1 == 21) or (p2 > 21 > p1) or (21 > p1 > p2):
                print("Player1 Win!")
            else:
                print("Player2 Win!")
        print("Player1 point :", p1)
        print("Player2 point :", p2)
    
class Player:
    def __init__(self):
        self.inHand = []
        self.status = False
        
    def getCard(self, card):
        self.inHand.append(card)
        
    def calculatePoint(self):
        self.point = 0
        for i in self.inHand:
            if i[0] in ["K", "Q", "J"]:
                self.point += 10
            elif i[0] == "A":
                acePoint = int(input("Choose 'A' point (1 or 11):"))
                self.point += acePoint
            else:
                self.point += i[0]
                                
deck = Deck()

gm = GM(deck.cards)

player1 = Player()
player1.getCard(gm.giveCard())
player1.getCard(gm.giveCard())

player2 = Player()
player2.getCard(gm.giveCard())
player2.getCard(gm.giveCard())

for i in range(3):
    print(player1.status)
    print(player2.status)
    if player1.status == True and player2.status == True:
        break
        
    if (player2.status == True and player1.status == False) or (player2.status == False and player1.status == False):
        print("Player1 Turn!")
        print("Player1 cards :", player1.inHand)
        player1.calculatePoint()
        print("Player1 point :", player1.point)
        choose = input("hit or stand :")
        if choose == "hit":
            player1.getCard(gm.giveCard())
            print("Player1 hit...")
        else:
            player1.status = True
            print("Player1 stand...")
        
    if (player2.status == False and player1.status == True) or (player2.status == False and player1.status == False):
        print("Player2 Turn!")
        print("Player2 cards :", player2.inHand)
        player2.calculatePoint()
        print("Player2 point :", player2.point)
        choose = input("hit or stand :")
        if choose == "hit":
            player2.getCard(gm.giveCard())
            print("Player2 hit...")
        else:
            player2.status = True
            print("Player2 stand...")
                    
gm.showResult(player1.point, player2.point)
