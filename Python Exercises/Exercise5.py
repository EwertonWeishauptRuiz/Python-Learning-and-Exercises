import random

#https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
a = range(1, random.randint(1,50))
b = range(1, random.randint(1, 80))

resultList = []

for numberA in a:
    if( numberA in b):
        resultList.append(numberA)

print(resultList)            