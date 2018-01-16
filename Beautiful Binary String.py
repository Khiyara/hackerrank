a = int(input())
s = input()
count = 0
z = 0
for c in range(len(s)-3):
    if s[z:z+3] == "010":
        count += 1
        z+=2
    z += 1     
if count>0:
    print (count)
else:
    print ("0")
