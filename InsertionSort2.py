def printArray(a):
    x=""
    for number in a:
        x += str(number) + " "
    print (x)

def insertionSort(a):    
    for i in range(0, len(a)):
        j = i
        while (j > 0 and a[j] < a[j-1]):
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            j -= 1
        if (i != 0): printArray(a)
m = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)
