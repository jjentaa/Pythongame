'''
Blackjack game 1 player 1 dealer
'''
import random

class Deck:
    def __init__(self):
        self.suit = ["♠","♥","♦","♣"]
        self.number = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.cards =[]
        #create cards
        for i in self.number:
            for j in self.suit:
                self.cards.append([i, j])
        #shuffle card
        random.shuffle(self.cards)
        
    def giveCard(self):
        #give and remove card
        return self.cards.pop(0) 
    
class Player:
    def __init__(self):
        self.inHand = [] #cards in hand
        self.status = False #False = not stand, True = stand
        
    def getCard(self, card):
        #get card from deck and add inHand
        self.inHand.append(card)
        
    def calculatePoint(self):
        self.point = 0
        countcard = 0 #used card 
        for i in self.inHand: 
            if i[0] in ["J", "Q", "K"]: 
                self.point = self.point + 10 
                countcard = countcard + 1 
            elif (i[0] == "A"): 
                pass
            else: 
                self.point = self.point + i[0]
                countcard = countcard + 1
                
        if countcard == len(self.inHand): 
            pass
        else: 
            if self.point <= 10:  
                self.point = self.point + 11
            else: 
                self.point = self.point + 1        

class Dealer(Player):
    def __init__(self):
        Player.__init__(self)
        
    def dicide(self):
        # decide method
        if self.point < 17:
            return "hit"
        else:
            return "stand"
    

class BlackJack:
    def __init__(self, deck, dealer, player1):
        self.deck = deck
        self.dealer = dealer
        self.player1 = player1
        self.dealer.getCard(self.deck.giveCard())
        self.dealer.getCard(self.deck.giveCard())
        self.player1.getCard(self.deck.giveCard())
        self.player1.getCard(self.deck.giveCard())

    def process(self):
        #process the game
        for i in range(1, 4):
            print(f"Round {i}!")
            #dealer and player all stand
            if self.player1.status == True and self.dealer.status == True:
                break
                
            #player1 not stand or dealer stand
            if self.player1.status == False or self.dealer.status == True:
                print("Player1 turn!")
                print(f"Player1 card : {self.player1.inHand}")
                self.player1.calculatePoint()
                print(f"Player1 point : {self.player1.point}")
                choose = input("hit or stand :")
                if choose == "hit":
                    self.player1.getCard(self.deck.giveCard())
                    print("Player1 hit...")
                else:
                    self.player1.status = True
                    print("Player1 stand...")
            print("---------------------------------")
            #player1 stand or dealer not stand
            if self.player1.status == True or self.dealer.status == False:
                print(self.dealer.inHand[0])
                self.dealer.calculatePoint()
                if self.dealer.dicide() == "hit":
                    self.dealer.getCard(self.deck.giveCard())
                    print("Dealer hit...")
                else:
                    self.dealer.status = True
                    print("Dealer stand...")
            print("---------------------------------")
    
    def showResult(self):
        print("The result is ...")
        #All lost
        if self.player1.point > 21 and self.dealer.point > 21:
            print("All Bust!")
        else:
            #Draw
            if self.player1.point ==  self.dealer.point:
                print("Draw")
            #player1 win
            elif (self.player1.point == 21) or ( self.dealer.point > 21 > self.player1.point) or (21 > self.player1.point >  self.dealer.point):
                print("Player1 Win!")
            #dealer win case
            else:
                print("Dealer Win!")
        print(f"Dealer point : {self.dealer.point}")
        print(f"Player1 point :{self.player1.point}")

deck = Deck() #create deck
dealer = Dealer() #create dealer
player1 = Player() #create player1
blackJack = BlackJack(deck, dealer, player1) #create game
blackJack.process() #process game
blackJack.showResult() #show result
