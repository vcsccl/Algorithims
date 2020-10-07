""" Insert Sort

    Jon Palmer
    CS 325 Fall 2020
    Last Edit: 10/06/2020

    Description:  Reads file, stores input string as array, 
    sorts array decrementally using insertion sort, and 
    outputs to file.  
"""

# Read file and store as string
inPut_in = []
with open("data.txt", "r") as inFile:
    for line in inFile:
        inPut_in.extend(map(int, line.split(' ')))

# Sort array decrementally using insertion sort 
def insertSort(inArray):
    for i in range(1, len(inArray)):
        key = inArray[i]
        j = i - 1
        while j >= 0 and inArray[j] < key:
            inArray[j + 1] = inArray[j]
            inArray[j] = key
            j -= 1
    return inArray

# Output to file
outArray = insertSort(inPut_in)
inPut_out = " ".join(map(str, outArray))
writeFile = open("insert.out", "x")
writeFile.write(inPut_out)
writeFile.close()