import sys

def funnyString(s):
    r = s[::-1]
    k = []
    for x in range(len(s)):
        d1 = abs(ord(s[x]))-abs(ord(s[(x-1)]))
        d2 = abs(ord(r[x]))-abs(ord(r[(x-1)]))
        if d1 != d2:
            print ("Not Funny")
            break
    else:
        print ("Funny")
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    funnyString(s)
