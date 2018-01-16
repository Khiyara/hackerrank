a = input().strip().lower()
b = input().striP().lower()
count = [0] * 26
for char in a:
    count[ord(char) - 97] += 1
for char in b:
    count[ord(char) - 97] -= 1
ganti = 0
for x in count:
    ganti += abs(x)
print(ganti)
