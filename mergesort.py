""" Merge Sort

    Jon Palmer
    CS 325 Fall 2020
    Last Edit: 10/06/2020

    Description:  Reads file, stores input string as an array, 
    sorts array decrementally using merge sort, and 
    outputs to file.  

"""

# Read file and store as array
inPut_in = []
with open("data.txt", "r") as inFile:
    for line in inFile:
        inPut_in.extend(map(int, line.split(' ')))

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

# Output to file
outArray = mergeSort(inPut_in)
inPut_out = " ".join(map(str, outArray))
writeFile = open("merge.out", "x")
writeFile.write(inPut_out)
writeFile.close()