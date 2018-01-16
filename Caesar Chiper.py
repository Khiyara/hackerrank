import string
integer = int(input())
huruf = input()
angka = int(input())
val=""
for x in huruf:
        c = ord(x)
        angka=angka%26
        if x in string.punctuation:
            val = val + x
            continue
        if (c > 64 and c<=90):
            c += angka
            if c > 90:
                c-=26
        elif (c>96 and c<=122):
            c+= angka
            if c > 122:
                c-=26
        val = val + chr(c)
print (val)
