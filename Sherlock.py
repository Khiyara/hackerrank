a = input()
huruf = [0] * 26
for x in a:
    huruf[ord(x)-97] += 1
while 0 in huruf:
    huruf.remove(0)
if max(huruf) - min(huruf) >= 1: print ("NO")
else: print("YES")

s = input()
distinctList = []
countList = []
for c in s:
    if c not in distinctList: distinctList.append(c)
for d in distinctList:
    count = s.count(d)
    countList.append(count)
key = countList[0]
flags = 0
for count in countList:
    if(key != count): flags+=1
if(flags > 1): print("NO")
else: print("YES")
