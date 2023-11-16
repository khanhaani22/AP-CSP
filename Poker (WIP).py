# POKER
import random
# By Haani Khan
class Spade:
    def __init__(self, card):
    self.card = "Spade"

class Heart(self, card):
    self.card = "Heart"
    
#Stating Variables
userCards = []
currentCards = []

#Cards
King = "K"
Queen = 'Q'
Jack = "J"
Ten = "10"
Nine = "9"
Eight = "8"
Seven = "7"
Six = "6"
Five = "5"
Four = "4"
Three = "3"
Two = "2"
Ace = "A"


#Declaring tables
SpadeDeck = [King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two, Ace]
DiamondDeck = [King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two, Ace]
CloverDeck = [King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two, Ace]
HeartDeck = [King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two, Ace]
Deck = [SpadeDeck, DiamondDeck, CloverDeck, HeartDeck]

currentCards.append(random.choices(Deck, k=3))
for card in currentCards:
    print(card)



