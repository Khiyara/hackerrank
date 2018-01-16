import sys
q = int(input().strip())
for x in range(q):
    s = input().strip()
    a="hackerrank"
    c=0
    for i in s:
        if i==a[c]:
            c+=1
        if c==10:
            break
    if c==10:
        print ("YES")
    else:
        print ("NO")
"""
d = int(input().strip())
for x in range(d):
    s = input().strip()
    fix = "hackerrank"
    k = []
    for c in s:
        if c == "h" or c=="a" or c=="c" or c=="k" or c=="e" or c=="r" or c=="n":
            k.append(c)
    k = "".join(k)
    for i in range(len(k)):
        if k[i:i+10] == fix:
            print ("YES")
            break
    else:
        print ("NO")
"""
