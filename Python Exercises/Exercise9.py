#https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

number = random.randint(1,9)
guess = 0
guesses = 0

while guess != number and guess != "exit":
    guess = input("What is your guess? \n")

    if(guess == "exit"):
        break

    guess = int(guess)
    guesses += 1

    if(guess > number):
        print("you guesses to high")

    elif(guess < number):
        print("You guesses to low")

    else:
        print("You got it right in " + str(guesses) + " guesses")
