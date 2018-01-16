a = int(input())
k=[]
for x in range(a):
    s = input().strip().split(" ")
    k.append([int(s[0]),s[1]])
d = []
v = 0
while True:
    for x in k:
        if x[0]==v:
            d.append(x)
    v+=1
    if len(d) == len(k):
        break
for x in d:
    if len(x[1])==2:
        if abs(ord(x[1][0])-ord(x[1][1]))==1:
            print ("-",end=" ")
        else:
            print(x[1],end=" ")
    else:
        print (x[1],end=" ")

n = int(input())
ar = []
for i in range(0,n) :
    data = input().strip().split(' ')
    ar.append((int(data[0]), data[1]))

c = [0]*100
for a in ar :
    c[a[0]] += 1
    
c1 = [0]*100
for x in range(1,100) :
    c1[x] = c1[x-1] + c[x-1]

s = ['-']*n
for i in range(0,n) :
    if i >= n/2 :
        s[c1[ar[i][0]]] = ar[i][1]
    c1[ar[i][0]] += 1
    
print(' '.join(s))
