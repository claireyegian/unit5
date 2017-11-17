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
print('Min:',min(numbers))
print('Max:',max(numbers))
if len(numbers)%2==0:
    print('Median:',numbers[len(numbers)/2 - 1],',',numbers[len(numbers)/2])
print('Mean:',sum(numbers)/len(numbers))
print('Mode:',!!!!!!!!!!!!!!!!!!!)
