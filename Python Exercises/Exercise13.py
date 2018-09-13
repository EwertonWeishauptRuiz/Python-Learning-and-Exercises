#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
#The Fibonnaci seqence is a sequence of numbers where the next number in 
#the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this

amount = int(input("How many number from the sequence"))
counter = 0
fibonnaci = []

def NextNumber():
    return (fibonnaci[len(fibonnaci) -2]) + fibonnaci[(len(fibonnaci) -1)]

if(amount == 1):
    fibonnaci = [1]
elif(amount == 2):
    fibonnaci = [1, 1]
else:    
    fibonnaci = [1, 1]
    while counter < amount:
        fibonnaci.append(NextNumber())
        counter += 1

print(fibonnaci)