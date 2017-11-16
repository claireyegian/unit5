#Claire Yegian
#11/15/17
#randomMonth.py - prints random month of the year

from random import randint

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
randomNumber = randint(0,11)
print(months[randomNumber])
