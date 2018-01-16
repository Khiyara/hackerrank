a = input()
b = list(map(int, input().split()))
b.sort()
x = b[0]
z = 0
for c in b:
    if c == max(b):
        print(b[z-1])
        break
    z += 1

