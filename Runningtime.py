def insertionSort(m,ar):
    shift = 0
    if m < 2:
        print(shift)
    else:
        for x in range(1,m):
            while ar[x] < ar[x-1]:
                ar[x], ar[x-1] = ar[x-1],ar[x]
                shift += 1
                if x > 1:
                    x -= 1
        print(shift)
m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(m, ar)

