#Claire Yegian
#11/15/17
#longestWord.py - indentifies longest word in list

words = input('Enter a list of words: ').split(' ')

longestWord = 0
listLength = len(words)
longestword = ''
i = 0
while i<(listLength):
    word = words[i]
    if len(word)>=longestWord:
        longestWord = len(word)
        longestword = word
    i += 1

print(longestword)
