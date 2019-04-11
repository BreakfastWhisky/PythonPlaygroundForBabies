#Blackjack with Daniel

# This version ~deliberately~ is not using functions, objects, or fancy tools as
# This is for the baby programmers

import random

# Title screen here. TODO Make titlescreen cooler
print("=============================================")
print("           Blackjack with Daniel")
print("                   Ver 0.01                  ")
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
bet = int(input("You have $%s. How much do you want to bet? " % playerCash))
playerCash = playerCash - bet

#deal the cards
#TODO Make it so cards are actually dealt from a deck that keeps track of which cards have been dealt

# For now, I will just treat the cards as a random number between 1 and 13
dealerCard1 = random.randint(1, 14)
dealerCard2 = random.randint(1, 14)

playerCard1 = random.randint(1, 14)
playerCard2 = random.randint(1, 14)

#figure out the name for the dealer's first card
if dealerCard1 == 1:
    dealerCard1Name = "Ace"
elif dealerCard1 == 11:
    dealerCard1Name = "Jack"
elif dealerCard1 == 12:
    dealerCard1Name = "Queen"
elif dealerCard1 == 13:
    dealerCard1Name = "King"
else:
    dealerCard1Name = str(dealerCard1)

print("The dealer has a %s showing." % dealerCard1Name)

#Figure out the name for the player's first card
if playerCard1 == 1:
    playerCard1Name = "Ace"
elif playerCard1 == 11:
    playerCard1Name = "Jack"
elif playerCard1 == 12:
    playerCard1Name = "Queen"
elif playerCard1 == 13:
    playerCard1Name = "King"
else:
    playerCard1Name = str(playerCard1)

#Figure out the name for the player's second card
if playerCard2 == 1:
    playerCard2Name = "Ace"
elif playerCard2 == 11:
    playerCard2Name = "Jack"
elif playerCard2 == 12:
    playerCard2Name = "Queen"
elif playerCard2 == 13:
    playerCard2Name = "King"
else:
    playerCard2Name = str(playerCard2)


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
