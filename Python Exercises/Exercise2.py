#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
number = int(input("Type a number \n"))
check = int(input("Number to divide it by \n"))

if (number % 4 == 0):
    print(number, " is a multiple of 4")
elif (number % 2 == 0):
    print(number, " is an even number")
else:
    print(number, " is an odd number")

if (number % check == 0):
    print(number, " divides evenly by ", check)
else:
    print(number, " does not divide evenly by ", check)