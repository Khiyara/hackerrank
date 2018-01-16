a = input()
k=[]
b = int(input())
s = input().split()
for x in s:
    k.append(x)
    if int(x) == int(a):
        break
print (len(k)-1)
