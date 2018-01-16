a = int(input())
s = input().split()
valid = True
b = -1
c = s[-1]
while valid:
    try:
        if c < s[b-1]:
            s[b] = s[b-1]
        else:
            s[b] = c
            valid = False
        print (" ".join(s))
        b-=1
    except:
        s[0] = c
        print (" ".join(s))
        break
