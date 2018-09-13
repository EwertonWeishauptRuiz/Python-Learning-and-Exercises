#https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def RemoveSpaces(textInput):
    result = textInput.split()
    return result

def ReverseString(textInput):
    noSpaces = RemoveSpaces(textInput)
    reversedList = list(reversed(noSpaces))
    result = " ".join(reversedList)
    return result

myString = raw_input("give me a text to reverse\n")

print(ReverseString(myString))    