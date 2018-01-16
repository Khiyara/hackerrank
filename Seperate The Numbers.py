for c in range(int(input())):
    s = input().strip()
    n = len(s)
    x = ''
    for i in s[:-1]:
        x += i
        y = int(x)
        z = ''
        while len(z) < n:
            z += str(y)
            y += 1
        if n == len(z) and z == s:
            print("YES", x)
            break
    else: print("NO")







"""
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    
    x = -1
    for i in range(len(s) - 1):
        y = int(s[:i + 1])
        t = ''
        while len(t) < len(s):
            t += str(y)
            y += 1
        
        if t == s: x = int(s[:i + 1])
    
    if x == -1: print("NO")
    else: print("YES", x)

def sequence(s):
    x = int(s)
    ans = []
    tmp = s
    for i in range(x + 1, x + 40):
        tmp += str(i)
        ans.append(tmp)
    return ans

for x in range(int(input())):
    s = input()
    l = len(s)
    tmp = ""
    found = False
    for c in s:
        tmp += c
        if s in sequence(tmp):
            print("YES", tmp)
            found = True
            break
    if not found:
        print("NO")"""
