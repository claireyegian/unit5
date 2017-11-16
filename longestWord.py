#Claire Yegian
#11/15/17
#longestWord.py - indentifies longest word in list

words = input('Enter a list of words: ').split(' ')

longestWord = 0
listLength = len(words)
i = 0
while i<=(listLength+1):
    word = words[i]
    if len.word>=longestWord:
        longestWord = word
    i += 1