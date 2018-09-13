#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
myNumber = int(input("Give me a number: \n"))

x = range(2, myNumber + 1)
resultList = []

for number in x:
    if(myNumber % number == 0):
        resultList.append(number)

print(resultList)        