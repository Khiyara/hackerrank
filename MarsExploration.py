sos = input()
count = 0
for x in range(0,len(sos),3):
    val = sos[x:x+3]
    if val == "SOS":
        continue
    else:
        if val[0]!="S":
            count+=1
        if val[1]!="O":
            count+=1
        if val[2]!="S":
            count+=1
print (count)
