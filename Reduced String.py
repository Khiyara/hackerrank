s = input()
masuk = []
for i in range(len(s)):
    if not masuk or s[i] != masuk[-1]:
        masuk += [s[i]]
    else:
        masuk.pop()
if masuk:
    print ("".join(masuk))
else:
    print ('Empty String')
