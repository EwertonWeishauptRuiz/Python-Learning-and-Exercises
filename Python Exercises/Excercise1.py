# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
name = input("Type your name  \n")
age = int(input("Type your age \n"))
year = str((2018 - age) + 100)
print("Hi " + name + " you will turn 100 years old in the year " + year)