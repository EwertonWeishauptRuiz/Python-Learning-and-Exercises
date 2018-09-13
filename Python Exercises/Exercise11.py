#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def GetNumber(helpText):
    return int(input(helpText))

def CheckPrime(number):
    if(number == 1):
        isPrime = False
    elif(number == 2):
        isPrime = True
    else: 
        isPrime = True
        for checkNumber in range(2, (number / 2)+1):
            if (number % checkNumber == 0):
                isPrime = False
                break
    return isPrime

def PrintResult(number):
    prime = CheckPrime(number)
    if(prime):
        description = ""
    else:
        description = "not "
    print(str(number) + " is " + description + "prime.")

#Never Ending loop
while(1 == 1):
    PrintResult(GetNumber("Enter a number to check. CTRL+C to exit "))