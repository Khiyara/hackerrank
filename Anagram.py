a = int(input())
for x in range(a):
    s = input()
    b = 0
    count = 0
    str_list = []
    str_list.extend(s)
    if len(s)%2==1:
        print ("-1")
        continue
    z = str_list[0:len(s)//2]
    v = str_list[len(s)//2:]
    for c in range(len(z)):
        if z.count(v[c])!=0:
            print (z)
            z.remove(v[c])
            print (z)
        else:
            count +=1
    print (count)
            
