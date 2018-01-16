import string
s = input().strip()
count = 1
for x in s:
    if x in string.ascii_uppercase:
        count+=1
print (count)
        
    
    
