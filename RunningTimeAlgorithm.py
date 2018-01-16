a = int(input())
s = input().split()
k = []
for x in s:
    k.append(int(x))
count = 0
if a < 2:
    print (count)
else:
    for x in range(1,a):
        while k[x] < k[x-1]:
            k[x], k[x-1] = k[x-1], k[x]
            count += 1
            if x > 1:
                x-=1
    print (count)
