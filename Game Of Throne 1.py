import sys
a = input()
huruf = [0] * 26
for x in a:
    huruf[ord(x) - 97] += 1
k = []
for c in huruf:
    k.append(str(c))
k = " ".join(k)
k=k.split(" ")
while "0" in k:
    k.remove("0")
k.sort()
k="".join(k)
c = set(k)
if len(c) == 1:
    print ("NO")
    sys.exit()
for x in range(len(k)-2):
    if k[x]!=k[x+1] and k[x+1] != k[x+2]:
        print ("NO")
        break
else:
    print ("YES")


##############

s = input()
cnt = {}
for char in s:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1
odd = False
for key in cnt:
    if cnt[key] % 2 == 1:
        if odd:
            print("NO")
            break
        odd = True
else:
    print("YES")    
        
