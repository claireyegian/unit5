#Claire Yegian
#11/14/17
#listDemo.py - print out the first and last word in a list

words = input('Enter a list of words: ').split(' ')

#print out the list one item per line
for w in words:
    print(w)

print('The first word is', words[0])
print('The last word is', words[-1])