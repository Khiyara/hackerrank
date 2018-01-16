a = int(input())
s = input().split()
k = []
for x in s:
    k.append(int(x))
k.sort()
for x in k:
    print (x,end=" ")
    
