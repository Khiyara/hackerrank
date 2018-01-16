import sys

def palindromeIndex(s):
    k = []
    for i in s:
        k.append(i)
    for x in range(len(k)):
        c = k[:]
        c.pop(x)
        v = "".join(c)
        if v == v[::-1]:
            print (x)
            break
    else:
        print ("-1")
            
                
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    palindromeIndex(s)

