#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
myInput = int(input("Give a number to check the list \n"))
myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

for number in myList:
    if(number > myInput):
        newList.append(number)

print("Complete list: " + str(newList))