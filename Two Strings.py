import sys

def twoStrings(s1, s2):
    valid = True
    for x in s1:
        if valid == False:
            break
        for c in s2:
            if x == c:
                print ("YES")
                valid = False
                break
    else:
        print ("NO")

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip().lower()
    s2 = input().strip().lower()
    twoStrings(s1, s2)

berapa = int(input())
for x in range(berapa):
    a = input()
    b = input()
    Truea = [False] * 26
    Trueb = [False] * 26
    for char in a:
        Truea[ord(char) - 97] = True
    for char in b:
        Trueb[ord(char) - 97] = True
    for i in range(26):
        if Truea[i]==True and Trueb[i]==True:
            print("YES")
            break
    else:
        print("NO")
