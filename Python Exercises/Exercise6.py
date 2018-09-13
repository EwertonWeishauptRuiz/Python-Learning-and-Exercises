#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
myInput = input("Give me a word to check> \n")

if(myInput == myInput[::-1]):
    print("yes it is a palindrome")
else:
    print("Not a palindrome")