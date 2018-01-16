angka = int(input())
angka1 = int(input())
angka2 = list(map(int, input().strip().split(' ')))
k = []
for c in angka2:
    for v in angka2:
        if (c+v) == angka1:
            k.append((c,v))
        for b in angka2:
            if (c+v+b) == angka1:
                k.append((c,v,b))
            for n in angka2:
                if (c+b+v+n) == angka1:
                    k.append((c,v,b,n))
                for m in angka2:
                    if (c+v+b+n+m) == angka1:
                        k.append((c,v,b,n,m))
k.sort()
s = set(k)
print (s)
print (len(s))
            
