#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random

randomWords = ["chesse", "pizza", "wasd"]
randomBigLetters = ["A", "B", "C"]
randomSymbol = ["@", "%", "$"]
def GenerateWeakPassword():
    return randomWords[random.randint(0,2)]

def GenerateMediumPassword():
    return randomWords[random.randint(0,2)] + str(random.randint(0, 15))

def GenerateStrongPassword():
    return randomWords[random.randint(0,2)] + str(random.randint(0, 15)) + randomBigLetters[random.randint(0,2)] + randomSymbol[random.randint(0,2)]

choice = raw_input("Choose how strong you want your password(weak, medium, strong)\n")

if (choice == "weak"):
    print(GenerateWeakPassword())
elif(choice == "medium"):
    print(GenerateMediumPassword())
else:
    print(GenerateStrongPassword())

# Another result

# import string
# import random

# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password?'))))