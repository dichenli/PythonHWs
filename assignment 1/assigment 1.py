#Written by Dichen Li
#CIT 591 assignment 1
#initialize parameters
money_human = 100 #The money that the human player owns
money_computer = 100 #The money that the computer owns
maximum_bet = 10 #The maximum amount of money to bet each time
print "welcome to the game! You're playing with Dichen. The maximum bet each time is", maximum_bet, 'pesos.'
print "You have", money_human, "pesos.", "Dichen has", money_computer, "pesos."

#let the human player choose odd or even
side = raw_input("What side do you want? Input odd or even: ") #side is either odd or even
while side != "odd" and side != "even": #In case the input is not odd or even, let the player type again
    print "Error. Input \"odd\" or \"even\"" 
    side = raw_input("What side do you want? Input odd or even:")

#initialize game
print "\nGame begins!\n"
print "How many pesos do you bet this time?\
 Input an integer number from 1 to %d. You can enter 0 to end the game." % maximum_bet
import random #allows random number for the computer's bet

#One loop for each bet
while money_human >= 2 * maximum_bet and money_computer >= 2 * maximum_bet: #Game continues until one side loses
    bet_computer = random.randint(1, maximum_bet) #Computer bets randomly
    bet_human = input("You bet: ") #human bets
    if bet_human == 0: #If human wants to quit
        print "You ended the game! "
        break #end the game
    while bet_human > maximum_bet or bet_human < 0 or bet_human % 1 != 0: # In case the human player bets by an invalid value.
        print "Error! You must bet an integer between 1 and %d! You can enter 0 to end the game" % maximum_bet
        bet_human = input("Please bet again: ")
    if bet_human == 0: #If human wants to quit after the correction above
        print "You ended the game! "
        break
    sum_bet = bet_human + bet_computer #sum_bet is the sum of two players' bets
    if (sum_bet % 2 == 0 and side == "even") or (sum_bet % 2 == 1 and side == "odd"): #conditions that makes the human win
        money_human = money_human + sum_bet
        money_computer = money_computer - sum_bet
        print "Dichen bets:", bet_computer, "\nYou win this bet!"
    else: # if computer wins
        money_computer = money_computer + sum_bet
        money_human = money_human - sum_bet
        print "Dichen bets:", bet_computer, "\nDichen wins this bet!"
    print "You have %d, Dichen has %d." % (money_human, money_computer)

#Game ends. Two results
if money_human < 2 * maximum_bet: 
    print "Sorry, you lose the game."
elif money_computer < 2 * maximum_bet:
    print "Congratulations! You win!"

    
