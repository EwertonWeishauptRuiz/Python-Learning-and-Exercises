#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import random

global myChoice

def waitForInput():
    myChoice = input("Choose Rock, Paper or Scissors or type Q to quit\n==>Use R, P or S\n")
    playerPlay(myChoice)   

def playerPlay(playerInput):
    if(playerInput == "R" or playerInput == "r"):
        checkWinner(0)
    elif (playerInput == "P" or playerInput == "p"):
        checkWinner(1)
    elif (playerInput == "S" or playerInput == "s"):
        checkWinner(2)     
    elif (playerInput == "Q" or playerInput == "q"):
        print("Exiting....")
        return
    else:
        print("Not a valid input....")
        waitForInput()

def checkWinner(playerPlay):
    computerPlay = random.randint(0,2)         
    if(playerPlay == computerPlay):
        print("It is a tie")
    elif(playerPlay == 0):
        if(computerPlay == 1):
            print("Player chose Rock, PC chose Paper\nComputer Wins")
        else:
            print("Player chose Rock, PC chose Scissors\nPlayer Wins")
    elif(playerPlay == 1):            
        if(computerPlay == 0):
            print("Player chose Paper, PC chose Rock\nPlayer wins")
        else:
            print("Player chose Paper, PC chose Scissors\nComputer Wins")
    else:
        if(computerPlay == 0):
            print("Player chose Scissors, PC chose Rock\nComputer wins")
        else:
            print("Player chose Scissors, PC chose Papers\nPlayer Wins")
    playAgain = input("Play another game?\n=>Y/N\n")        
    if(playAgain == "Y" or playAgain == "y"):        
        waitForInput()
    else:
        print("Exiting...")
        return

waitForInput()     


         
    
       