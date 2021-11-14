import numpy as np
import math as mt
import time



def getUserInput(displayMessage, inputType):
    userInput = input(displayMessage)
    if inputType == int:
        while type(userInput) != int:
            try:
                userInput = int(userInput)
            except:
                userInput = input(displayMessage)
    return userInput



def testIsPrimeNumber(testNumber):
    squareRoot = np.sqrt(testNumber)
    testLimit = int("{:.0f}".format(squareRoot)) + 1
    for element in range(testLimit):
        if (testNumber % (element+1) == 0) and ((element+1) not in (1, testNumber)):
            return False
    return True



def choosePrimesNumbers():
    isPrimeNumber = False
    while isPrimeNumber != True:
        number = getUserInput(displayMessage = 'Choose a prime number : ', inputType = int)
        isPrimeNumber = testIsPrimeNumber(number)
    return number



def getBobParameters():
    n = 0
    while n < 255:
        print('Choose two prime numbers. Their product must be greater than 200.')
        p = choosePrimesNumbers()
        q = choosePrimesNumbers()
        n = p * q
    return n, p, q



def testIsRelativelyPrime(firstNumber, testNumber):
    gcd = mt.gcd(firstNumber, testNumber)
    if gcd == 1 and testNumber < firstNumber:
        return True
    else:
        return False



def chooseRelativelyPrimeNumber(phi):
    isRelativelyPrime = False
    while isRelativelyPrime != True:
        number = getUserInput(displayMessage = 'Choose a number relatively prime to ' + str(phi) + ' : ', inputType = int)
        isRelativelyPrime = testIsRelativelyPrime(phi, number)
    return number



def getPrivateKey(phi, e):
    for number in range(1, phi-1):
        if (e*number)%phi == 1:
            d = number
            break
    return d



def getAliceParameters(p, q):
    phi = (p-1)*(q-1)
    e = chooseRelativelyPrimeNumber(phi)
    d = getPrivateKey(phi, e)
    return phi, e, d



def getMessageUnicode(message):
    messageUnicode = []
    for character in message:
        messageUnicode.append(ord(character))
    return messageUnicode



def getUserMessage():
    messageInitial = getUserInput(displayMessage = 'Enter a message to encrypt : ', inputType = str)
    messageUnicode = getMessageUnicode(messageInitial)
    return messageUnicode



def encryptMessage(n, e):
    message  = getUserMessage()
    cryptMessage = []
    for character in range(0, len(message)):
        cryptCharacter = (message[character]**e)%n
        cryptMessage.append(cryptCharacter)
    return cryptMessage



def decryptMessage(cryptMessage, n, d):
    message = ''
    for character in range(0, len(cryptMessage)):
        decryptCharacter = (cryptMessage[character]**d)%n
        unicodeCharacter = chr(decryptCharacter)
        message = message + unicodeCharacter
    return message



def getPrimeDecompostion(number): 
    divisor = 2
    listDivisors = []
    while divisor <= number:
        if number%divisor == 0:
            listDivisors.append(divisor)
            number = number/divisor
        else:
            divisor += 1
    if len(listDivisors) == 1:
        listDivisors.append(1)
    firstDivisor = listDivisors[0]
    secondDivisor = listDivisors[1]
    return firstDivisor, secondDivisor



def crackMessage(cryptMessage, n, e):
    startTimer = time.time()
    p, q = getPrimeDecompostion(n)
    phi = (p-1)*(q-1)
    d = getPrivateKey(phi, e)
    crackedMessage = decryptMessage(cryptMessage, n, d)
    endTimer = time.time()
    timer = round(endTimer - startTimer, 4)
    print('Message cracked in : ' + str(timer) + ' seconds')
    return crackedMessage