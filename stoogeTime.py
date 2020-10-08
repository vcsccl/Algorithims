""" Stooge Time

    Jon Palmer
    CS 325 Fall 2020
    Last Edit: 10/06/2020

    Description:   Stooge sort implementation that generates arrays of size n 
    containing random integer values, records the time taken to sort, and
    outputs runs/average to CSV.  
"""
import os 
import time 
import random

# Generate arrays of n size and output nested list
n1 = 500
n2 = 1000
n3 = 1500
n4 = 2000
nIn = [[0]*n1, [0]*n2, [0]*n3, [0]*n4]
nOut = [[n1],[n2],[n3],[n4]]

# Sort arrays using stooge sort
def stoogeSort(inArray, l, h):
    a = h - l + 1
    if (a == 2) and (inArray[l] > inArray[h]):
        t = inArray[l]
        inArray[l] = inArray[h]
        inArray[h] = t
    elif a > 2: 
        m = (int)((a) / 3)
        stoogeSort(inArray, l, (h - m))
        stoogeSort(inArray, l+t, (h))
        stoogeSort(inArray, l, (h - m))
    else:
        return
    return inArray

# Fill and record arrays 
def printOut(inArray, mIt):
    avgTime = 0
    for k in range(1, 8):
        tempTime = 0
        for l in range(0, len(inArray)):
            inArray[l] = random.randint(0, 10000)
        startTime = time.time()
        stoogeSort(inArray, 0, (len(inArray)-1))
        tempTime += time.time() - startTime
        nOut[mIt].insert(k, tempTime)
        avgTime = avgTime + tempTime
    avgTime = avgTime / 7
    nOut[mIt].extend([avgTime])

# Definition call
ki = 0
for a in nIn:
    printOut(a, ki)
    ki += 1
    
# Convert to string and utput to Terminal
inPut_out = ""
for i in nOut: 
    inPut_out += ", ".join(map(str, i)) + "\n"
print(inPut_out)

# Write to file
if os.path.exists("test.txt"):
    os.remove("test.txt")
writeFile = open("test.txt", "x")
writeFile.write(inPut_out)
writeFile.close()
