a = int(input())
for x in range(a):
    s = input()
    val = 0
    p = []
    for c in s:
        if c not in p:
            val += 1
            p.append(c)
    print (val)
