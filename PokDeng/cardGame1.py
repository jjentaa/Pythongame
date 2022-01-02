'''PokDeng 2 players'''
import random

class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def display(self):
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
        self.cardInHand = []
        self.name = name

    def getCard(self, card):
        self.cardInHand.append(card)

    def showCard(self):
        for c in self.cardInHand:
            c.display()

    def calculatePoint(self):
        self.point = 0
        for a in self.cardInHand:
            if a.number in ["K", "Q", "J"]:
                self.point += 0
            elif a.number == "A":
                self.point += 1
            else:
                self.point += a.number

        self.point = self.point % 10

        return self.point 

    def checkPok(self):
        self.pok = [False, "-"]
        for a in self.cardInHand[1: len(self.cardInHand)]:
            if a.number == self.cardInHand[0].number:
                self.pok = [True, a.number]
            else:
                self.pok = [False, "-"]
            
    def checkTong(self):
        self.tong = [False, "-"]
        if len(self.cardInHand) == 3:
            for a in self.cardInHand[1: len(self.cardInHand)]:
                if a.number == self.cardInHand[0].number:
                    self.tong = [True, a.number]
                else:
                    self.tong = [False, "-"]

class PokDeng:
    def __init__(self, deck, player1, player2):
        self.deck = deck
        self.p1 = player1
        self.p2 = player2

    def startGame(self):
        print("Start Game")
        print(f"It's {self.p1.name}'s turn")
        self.p1.getCard(self.deck.giveCard())
        self.p1.getCard(self.deck.giveCard())
        self.p1.showCard()
        self.p1.checkPok()
        self.p1.checkTong()
        #print(self.p1.pok)
        #print(self.p1.tong)
        print(f"{self.p1.name}'s point : {self.p1.calculatePoint()}")
        chioce1 = input("Do want to draw more? (Y or N) :")
        if chioce1 == "Y":
            self.p1.getCard(self.deck.giveCard())
            self.p1.showCard()
            print(f"{self.p1.name}'s point : {self.p1.calculatePoint()}")

        print("---------------------------")    
        print(f"It's {self.p2.name}'s turn")
        self.p2.getCard(self.deck.giveCard())
        self.p2.getCard(self.deck.giveCard())
        self.p2.showCard()
        self.p2.checkPok()
        self.p2.checkTong()
        #print(self.p2.pok)
        #print(self.p2.tong)
        print(f"{self.p2.name}'s point : {self.p2.calculatePoint()}")
        chioce2 = input("Do want to draw more? (Y or N) :")
        if chioce2 == "Y":
            self.p2.getCard(self.deck.giveCard())
            print(f"{self.p2.name}'s point : {self.p2.calculatePoint()}")
            print(f"{self.p2.name}'s point : {self.p2.calculatePoint()}")
        print("-----------------------------") 

    def judge(self):
        '''
        point more than
        pok dok same
        tong number same 3
        '''
        if self.p1.pok[0] == True and self.p1.pok[0] == True:
            if self.p1.pok[1] > self.p2.pok[1]:
                self.winner = self.p1.name
            elif self.p1.pok[1] < self.p2.pok[1]:
                self.winner = self.p2.name
            elif self.p1.pok[1] == self.p2.pok[1]:
                self.winner = "Draw!"
                
        elif self.p1.pok[0] == True and self.p1.pok[0] == False:
            self.winner = self.p1.name
            
        elif self.p1.pok[0] == False and self.p1.pok[0] == True:
            self.winner = self.p2.name
        else:
            if self.p1.point > self.p2.point:
                self.winner = self.p1.name
            else:
                self.winner = self.p2.name

    def showWinner(self):
        print(f"The winner is {self.winner}.⭐️")

deck = Deck()

player1 = Player("Jane1")
player2 = Player("Jane2")

pok = PokDeng(deck, player1, player2)
pok.startGame()
pok.judge()
pok.showWinner()