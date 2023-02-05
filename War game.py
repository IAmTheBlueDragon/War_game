# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:47:42 2021

@author: Shreyas Om
"""
import random


#These are two tuples corresponding to the suit and ranks of the card
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')



#This is global dictionary is that corresponds the rank of the card to a integer value
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

'''
   eg:
       value[two_heats.rank] #This returns the integer value of for the card
'''



#This class is to intialize or create card for the game
class Card():
    def __init__(self,suit,rank):
        self.suit=suit      #Suit of the card
        self.rank=rank      #Rank of the card
        self.value=values[rank] #Integer value of the card
        
    def __str__(self):
        return(self.rank+"of"+self.suit)    #Prints the identitiy of the card
        
    '''
    eg:
        two_of_hearts = Card("Hearts","Two")
    '''



#This class creates a deck of all cards with each card havinf there own values and attributes
class Deck():
    def __init__(self):
        self.all_cards = [] #A list to hold all the cards
        
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = Card(suit, rank)
                #append the card object into the all cards list
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards) #Shuffling all the cards
    
    def deal_one(self):
        return(self.all_cards.pop()) #To get the first card of the deck and remove from the list
    
    '''
        eg:
            new_deck=Deck()
            new_deck.shuffle()
            new_deck.deal_one()
    ''' 



#Create a player calss that can initialize a hand and add and remove cards from the hand
class Player():
    
    def __init__(self,name):
        self.name = name    #Name of the player
        self.all_cards = []     #Initializing player hand
    
    def remove_one(self):
        return(self.all_cards.pop(0))   #Returns a card and removes it from the players hand
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):       #Checks wether the new_cards are a list or not
            self.all_cards.extend(new_cards) #Adds a new list of cards to player hand
        else:
            self.all_cards.append(new_cards)      #Adds a singular card to the players hand
    
    def __str__(self):
        return(f'Player {self.name}: has {len(self.all_cards)} cards.')
    
    '''
        eg:
            new_player=Player(Jose)
            new_player.remove_one
            new_player.add_cards(new_cards)
    '''       




''' ----------------------------------------------------------------------------------------------------------------- '''




#Game setup

player_one=Player('One')
player_two=Player('Two')

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on=True

round_num=0

while game_on:
    print(round_num)
    round_num+=1
    
    if len(player_one.all_cards)==0:
        print("Player One: Out of cards! Player two wins.")
        game_on=False
        break
    
    if len(player_two.all_cards)==0:
        print("Player Two: Out of cards! Player one wins.")
        game_on=False
        break
    
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    at_war= True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print("Round goes to player one.")
            at_war = False
            
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            print("Round goes to player two.")
            at_war = False
            
        else:
            print("War!!!!!!!")
            if len(player_one.all_cards)<5 and len(player_two.all_cards)>=5:
                print("Player One unable to declare war and hence player two wins")
                game_on=False
                break
            
            elif len(player_two.all_cards)<5 and len(player_one.all_cards)>=5:
                print("Player Two unable to declare war and hence player one wins")
                game_on=False
                break
            
            elif len(player_two.all_cards)<5 and len(player_one.all_cards)<5:
                print('None can declare war so one kill round.')
                one_kill=True
                while one_kill:
                    player_one_card=player_one.remove_one()
                    player_two_card=player_two.remove_one()
                    if player_one_card.value > player_two_card.value:
                        player_one.add_cards(player_one_cards)
                        player_one.add_cards(player_two_cards)
                        game_on=False        
                        one_kill = False
                                
                    elif player_two_card.value > player_one_card.value:
                        player_two.add_cards(player_two_cards)
                        player_two.add_cards(player_one_cards)
                        game_on=False        
                        one_kill = False
                        
                    else:
                        if len(player_one.all_cards)==0 and len(player_two.all_cards)>0:
                            print("Player One lost one kill and hence player two wins")
                            game_on=False
                            one_kill=False
                            break
                        
                        elif len(player_two.all_cards)==0 and len(player_one.all_cards)>0:
                            print("Player Two lost one kill and hence player one wins")
                            game_on=False
                            one_kill=False
                            break
                        
                        elif len(player_two.all_cards)==0 and len(player_one.all_cards)==0:
                            print("Draw")
                            game_on=False
                            one_kill=False
                            break
                    
                        else:
                            continue                  
                    
            
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    