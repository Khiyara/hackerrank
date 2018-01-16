q = int(input())
for a0 in range(q):
    s = input().strip()
    count = 0
    for x in range(len(s)-1):
        if s[x+1] == s[x]:
            count += 1
    print (count)
