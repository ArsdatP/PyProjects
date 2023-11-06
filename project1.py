import random

SCORE = 0

print("This is a game of Pig! In order to win your die must roll a 1. ")
print("if you wish to keep playing and risk all your balance, do it at your own accord.")

def roll():
    die = random.randrange(1,6)
    return die


def play():
    global SCORE

    while True:
        die = roll()
        if die == 1:
            print(f"You rolled a {die}. You lost all your points")
            break
        else:
            SCORE += die

            print(f"You rolled a {die}.")
            print(f"Your current score: {SCORE}")

            reply = input("Do you want to roll again (Y/N)? ").lower()
            if reply != "y":
                break




def menu():
    global SCORE

    while True:
        print("Welcome to my game of Pig!")
        print("If you would like to play, press `Y` or `N` to quit ")
        reply = input("> ")
        reply = reply.lower()

 
        if reply == "y":
            score = 0
            play()
            print(f"Your total score: {score}")
        elif reply == "n":
            print("Bye Bye")
            break
        else:
            print("Invalid Entry, try again.\n")





menu()






#test = roll()
#print(test)
