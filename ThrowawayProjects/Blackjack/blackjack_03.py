#Blackjack with Daniel

# Now let's be less awful.

import random

class card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        #Define the card's name
        if value == 1:
            self.cardName = "Ace of " + suit
        elif value == 11:
            self.cardName = "Jack of " + suit
        elif value == 12:
            self.cardName = "Queen of " + suit
        elif value == 13:
            self.cardName = "King of " + suit
        else:
            self.cardName = str(value) + " of " + suit

class deckOfCards:
    '''Handles a standard 52 card deck of of cards'''

    def __init__(self):
        # When creating the deck
        self.cards = []
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

        # Go through each of the four suits and...
        for x in suits:

            #Add one card of each value
            for y in range(13):
                tempCard = card(y+1, x)
                self.cards.append(tempCard)

        random.shuffle(self.cards)

        for x in self.cards:
            print(x.cardName)


gameDeck = deckOfCards()

#Function definitions
def dealCard():
    # TODO Still not tracking the deck of cards.
    card = random.randint(1, 14)
    return card

def nameCard(card):
    if card == 1:
        cardName = "Ace"
    elif card == 11:
        cardName = "Jack"
    elif card == 12:
        cardName = "Queen"
    elif card == 13:
        cardName = "King"
    else:
        cardName = str(card)

    return cardName


# Title screen here. TODO Make titlescreen cooler
print("=============================================")
print("           Blackjack with Daniel")
print("                   Ver 0.02                  ")
print("=============================================")
print()

input("Press Enter to Begin")

print()
print("You walk into an empty bar. It's a weekday night and the place is quiet. The faint smell of smoke wafts through the air.")
print("Standing behind the bar, in clothes that are a little too worn, is a blond haired man who appears to be in his twenties.")


playerName = input("Daniel: Hi there. Welcome to the Carpe Noctem. What's your name?\n")
# TODO in the future, user lookup code will go here.


print("Daniel: Good to have you, %s." % playerName)
print("Daniel: Please, have a seat.")

#Fuck Narration, I'm tired. Let's play blackjack

#new player Variables here
playerCash = 100

#handle betting
bet = int(input("You have $%s. How much do you want to bet? \n$" % playerCash))
playerCash = playerCash - bet

#deal the cards
#TODO Make it so cards are actually dealt from a deck that keeps track of which cards have been dealt

# For now, I will just treat the cards as a random number between 1 and 13
dealerCard1 = dealCard()
dealerCard2 = dealCard()

playerCard1 = dealCard()
playerCard2 = dealCard()

#figure out the names for the dealt cards

dealerCard1Name = nameCard(dealerCard1)
playerCard1Name = nameCard(playerCard1)
playerCard2Name = nameCard(playerCard2)

print("The dealer has a %s showing." % dealerCard1Name)
print("You have a %s and a %s." % (playerCard1Name, playerCard2Name))


#TODO TEMP For right now, let's just figure out the value of both player's hands and assign a winner
#BUG Jacks, Queens, and Kings are not being treated as though they were worth 10
#BUG Aces are not being treated as 1 or 10 dependent on the situation.

dealerTotal = dealerCard1 + dealerCard2
playerTotal = playerCard1 + playerCard2

if dealerTotal > 21:
    dealerTotal = -1
    print("The dealer busted out.")
else:
    print("The Dealer's hand is worth %s" % str(dealerTotal))

if playerTotal >21:
    playerTotal = -1
    print("You busted out.")
else:
    print("Your hand is worth %s" % str(playerTotal))

if playerTotal > dealerTotal:
    print("You won!")
    playerCash = playerCash + bet * 2
elif playerTotal < dealerTotal:
    print("The dealer won! He keeps your bet!")
else:
    print("You and the dealer tied! You get your bet back.")
    playerCash = playerCash + bet

print("You now have $%s." % str(playerCash))

#.... now, how EVER would we be able to repeat this to play a second game of Blackjack? A third?
# 30 games?
