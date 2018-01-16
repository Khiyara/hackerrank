a = int(input().strip().lower())
huruf = [0]*26
for x in range(a):
    string = sorted(input())
    res = ""
    for char in string:
        if res != char:
            res = char
            huruf[ord(ch) - 97] += 1

gemstone = 0
for item in huruf:
    if item == a:
        gemstone += 1
print(gemstone)


n = int(input())
first_input = set(input())

for i in range(n-1):
    rest_input = set(input())
    first_input = first_input & rest_input

print(len(first_input))
