#Claire Yegian
#11/17/17
#stat.py - outputs min, max, median, mean, and mode of list of numbers

numbers = []
i = ''
while i!='q':
    i = input('Enter a list of numbers: ')
    if i!='q':
        numbers.append(float(i))

numbers.sort()

def mode():
    numberOf = 0
    highestNumberOf = 0
    mostCommon = ''
    placement = 0
    for item in numbers:
        if item == numbers[placement-1]:
            numberOf = 2
            if numberOf>highestNumberOf:
                highestNumberOf = numberOf
                mostCommon = item
        placement += 1
    print('Mode:',mostCommon)
    
print('Min:',min(numbers))
print('Max:',max(numbers))
if len(numbers)%2==0:
    print('Median:',numbers[len(numbers)/2 - 1],',',numbers[len(numbers)/2])
print('Mean:',sum(numbers)/len(numbers))
mode()
