a = int(input())
for x in range(a):
    s = input()
    val = 0
    for c in range(len(s)//2):
        z = ord(s[c])
        v = ord(s[(len(s)-1)-c])
        if v != z:
            if z > v:
                val += z - v
            else:
                val += v - z
    print (val)
            
