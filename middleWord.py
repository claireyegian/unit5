#Claire Yegian
#11/15/17
#middleWord.py - prints middle words in list

words = input('Enter a list: ').split(' ')
midlist = words
length = int(len(midlist))
if length%2==0:
    print(midlist[(int(length/2) - 1):(int(length/2) + 1)])
if length%2!=0:
    print(midlist[(length-1)/2])