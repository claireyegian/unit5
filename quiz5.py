#Claire Yegian
#12/3/17
#quiz5.py - functions 1-3

from random import randint

def rand5():
    numberList = []
    i = 1
    while i<=5:
        numberList.append(randint(1,100))
        i += 1
    return numberList


def lastElement(list):
    return(list[(len(list)-1)])
    

def wordLengths(stringList):
    i = 0
    for item in stringList:
        stringList[i] = len(item)
        i += 1
    return(stringList)


def biggest(numberList):
    largestNumber = 0
    for item in numberList:
        if item > largestNumber:
            largestNumber = item
    return(largestNumber)

print(rand5())
print(lastElement(['cat','dog','rat']))
print(wordLengths(['the','cat','is','hungry']))
print(biggest([3,-1,5,-2,7,2,1]))
