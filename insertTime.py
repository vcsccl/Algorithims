""" Insert Time

    Jon Palmer
    CS 325 Fall 2020
    Last Edit: 10/06/2020

    Description:    
"""
import time 
import random

# Generate arrays of n size
n1 = [0] * 5000
n2 = [0] * 10000
n3 = [0] * 15000
n4 = [0] * 20000


# Sort arrays decrementally using insertion sort 
def insertSort(inArray):
    for i in range(1, len(inArray)):
        key = inArray[i]
        j = i - 1
        while j >= 0 and inArray[j] < key:
            inArray[j + 1] = inArray[j]
            inArray[j] = key
            j -= 1
    return inArray

# Output to Terminal
def printOut(inArray):
    tempTime = 0
    for k in range(0, 6):
        startTime = time.time()
        for l in range(0, len(inArray)):
            inArray[l] = random.randint(0, 10000)
        insertSort(inArray)
        tempTime += time.time() - startTime
    tempTime = tempTime / 7
    print("Array Size: " + str(len(inArray)) + " Time to Execute: " + str(tempTime))

printOut(n1)
printOut(n2)
printOut(n3)
printOut(n4)
