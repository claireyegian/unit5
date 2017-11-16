#Claire Yegian
#11/16/17
#warmup13.py - makes list and prints min, max, and sum

from random import randint

numbers = []
i = 0
while i<20:
    numbers.append(randint(9,99))
    i += 1

print(min(numbers))
print(max(numbers))
print(sum(numbers))
