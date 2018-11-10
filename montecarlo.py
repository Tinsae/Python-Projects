from random import randint
rounds = int(input('How many rounds would you like to play? '))
switching = input("Would you like to always stay or switch?")

for x in rounds:
    guess = int(input("Which door would you like to pick? "))
    car = randint (1,3) 
    print ("You picked Door #" + str (guess))

    # if user guessed correct
    if car == guess:
        if(car == 1):
            print("Their is a goat behind door ", 2)
        elif(car == 2):
            print("Their is a goat behind door ", 3)
        else:
            print("Their is a goat behind door ", 1)
        
        choice = input("would you like to change your pick?") 
        if(choice.lower() == "yes"):
            print("The car was behind Door #", car ,"!")
            print("You Lost")
        else:
            print("The car was behind Door #", car,"!")
            print("You Won")

    # user guessed wrong
    else:
        print("Their is a goat behind door ", 6 - car - guess)
        choice = input("would you like to change your pick?") 
        if(choice.lower() == "yes"):
            print("The car was behind Door #", car ,"!")
            print("You Win")
        else:
            print("The car was behind Door #", car ,"!")
            print("You Lost")
            
            
