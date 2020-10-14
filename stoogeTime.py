""" Stooge Time

    Jon Palmer
    CS 325 Fall 2020
    Last Edit: 10/06/2020

    Description:   Stooge sort implementation that generates arrays of size n 
    containing random integer values, and records the time taken to sort.  
"""
import os 
import time 
import random

n1 = 50
n2 = 100
n3 = 150
n4 = 200

nL1 = [] * n1
nL2 = [] * n2
nL3 = [] * n3
nL4 = [] * n4

nLi1 = [n1]
nLi2 = [n2]
nLi3 = [n3]
nLi4 = [n4]

nIn = [[], [], [], []]
nOut = [[n1],[n2],[n3],[n4]]

def main(array, size, output):
    avgTime = 0
    for e in range(size):
        array.append(random.randint(0, 10000))
        print(array)
        for axe in range(7):
            tempTime = 0
            startTime = time.time()
            stoogeSort(array, 0, (len(array) - 1))
            tempTime += time.time() - startTime
            output.append(tempTime)
 
    print(output)

def stoogeSort(inArray, i, j):
    n = j - i + 1
    if (n == 2) and (inArray[i] > inArray[j]):
        t = inArray[i]
        inArray[i] = inArray[j]
        inArray[j] = t
    if n > 2: 
        t = (int)((n) / 3)
        stoogeSort(inArray, i, (j - t))
        stoogeSort(inArray, i + t, (j))
        stoogeSort(inArray, i, (j - t))

def format(rawData):
    forData = ""
    for i in rawData: 
        forData += ", ".join(map(str, i)) + "\n"
    return forData

def write(forData):
    if os.path.exists("data.txt"):
        os.remove("data.txt")
    writeFile = open("data.txt", "x")
    writeFile.write(forData)
    writeFile.close()

main(nL1, n1, nLi1)
main(nL2, n2, nLi2)
main(nL3, n3, nLi3)
main(nL4, n4, nLi4)

forData = format(nOut)
write(forData)
