from random import randint
# while round is out of range
# ask user again
rounds = int(input('How many rounds would you like to play? '))
while(rounds < 10 and rounds > 10000):
    rounds = int(input('How many rounds would you like to play? '))
choice = input("Would you like to always stay or switch?")
while(choice != "stay" and choice != "switch"):
    choice = input("Would you like to always stay or switch?")
losses = 0
wins = 0
for x in range(rounds):
    # pick random door for player
    guess = randint(1,3)
    # pick random door to hide car
    car = randint (1,3) 
    # player guessed correct
    if car == guess:
        if(choice.lower() == "stay"):
            wins += 1
        else:
            losses += 1

    # user guessed wrong
    else:
        if(choice.lower() == "stay"):
            losses +=1
        else:
            wins +=1
print ("You won {:.2f} % times \n You Lost {:.2f} % times".format(wins/rounds * 100, losses/rounds *100))
