import string
list_huruf = list(string.ascii_lowercase)
huruf = input()
huruf_list = []
for x in range(len(huruf)):
    huruf = huruf.lower().replace(" ","")
for x in huruf:
    huruf_list.append(x)
huruf_list = set(huruf_list)
huruf_list = list(huruf_list)
valid = True
if len(huruf_list) < 26:
    valid = False
elif len(huruf_list) == 26:
    valid = True
if valid == True:
    print ("pangram")
else:
    print("not pangram")

