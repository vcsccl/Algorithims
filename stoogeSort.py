""" Stooge Sort

    Jon Palmer
    CS 325 Fall 2020
    Last Edit: 10/06/2020

    Description:   Implement STOOGESORT to sort an array/vector of integers. 
    The program reads input from a file called data.txt where the first 
    value of each line is the number of integers that need to be sorted, followed by the 
    integers. The output will be written to a file called stooge.out  
"""

#inPut_in = []
with open("data.txt", "r") as inFile:
    for line in inFile:
        inPut_in.extend(map(int, line.split(' ')))

# Sort array decrementally using stooge sort
def stoogeSort(inArray, l, h):
    a = h - l + 1
    if (a == 2) and (inArray[l] > inArray[h]):
        m = inArray[l]
        inArray[l] = inArray[h]
        inArray[h] = m
    elif a > 2: 
        m = (int)((h-l+1) / 3)
        stoogeSort(inArray, l, (h - m))
        stoogeSort(inArray, l + m, (h))
        stoogeSort(inArray, l, (h - m))
    else:
        return

    return inArray

# Output to file
outArray = stoogeSort(inPut_in, 0, (len(inPut_in) - 1))
inPut_out = " ".join(map(str, outArray))
print(inPut_out)
writeFile = open("stooge.out", "x")
writeFile.write(inPut_out)
writeFile.close()
