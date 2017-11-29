#Claire Yegian
#11/27/17
#mergeSort.py - implementation of merge sort

from random import randint
from time import time

N = 1000 #how many numbers will be sorted

"""function merge_sort(list m)
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of m ≤ 1 then
        return m

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    // Recursively sort both sublists.
    left := merge_sort(left)
    right := merge_sort(right)

    // Then merge the now-sorted sublists.
    return merge(left, right)"""

def mySort(A):
    if len(A)<=1:
        varLeft = []
        varRight = []
        for i in range(0,len(A)):
            if i < len(A)/2:
                varLeft.append(A[i])
            else:
                varRight.append(A[i])
        mySort(varLeft)
        mySort(varRight)

        merge(varLeft,varRight)

"""function merge(left, right)
    var result := empty list

    while left is not empty and right is not empty do
        if first(left) ≤ first(right) then
            append first(left) to result
            left := rest(left)
        else
            append first(right) to result
            right := rest(right)

    // Either left or right may have elements left; consume them.
    // (Only one of the following loops will actually be entered.)
    while left is not empty do
        append first(left) to result
        left := rest(left)
    while right is not empty do
        append first(right) to result
        right := rest(right)
    return result"""

def merge(left,right):
    result = []
    while len(left)!=0 and len(right)!=0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    
    while len(left)!=0:
        result.append(left[0])
        left = left[1:]
    while len(right)!=0:
        result.append(right[0])
        right = right[1:]
    
    return result

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
