#Claire Yegian
#11/30/17
#warmup15.py - doubles list of numbers

def double(numbers):
    numbers2 = []
    for item in numbers:
        item = item*2
        numbers2.append(item)
    return(numbers2)

print(double([3,4,6]))
