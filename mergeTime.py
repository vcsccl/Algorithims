""" Merge  Time

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

# Sort array decrementally using merge sort
def mergeSort(inArray):
    if len(inArray) > 1:
        leftArray = inArray[:len(inArray)//2]
        rightArray = inArray[len(inArray)//2:]
        
        mergeSort(leftArray)
        mergeSort(rightArray)
        
        i = 0
        j = 0
        k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] > rightArray[j]:
                inArray[k] = leftArray[i]
                i += 1
            else:
                inArray[k] = rightArray[j]
                j += 1
            k += 1
        
        while i < len(leftArray):
            inArray[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            inArray[k] = rightArray[j]
            j += 1
            k += 1

    return inArray

# Output to Terminal
def printOut(inArray):
    tempTime = 0
    for i in range(0, 6):
        startTime = time.time()
        for i in range(0, len(inArray)):
            inArray[i] = random.randint(0, 10000)
        mergeSort(inArray)
        tempTime += time.time() - startTime
    tempTime = tempTime / 7
    print("Array Size: " + str(len(inArray)) + " Time to Execute: " + str(tempTime))

printOut(n1)
printOut(n2)
printOut(n3)
printOut(n4)