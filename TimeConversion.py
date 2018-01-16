def timeConversion(s):
    s1 = s.split(":")
    val = int(s1[0])
    val1=str(val)
    if s.find("AM") == -1:
        if val == 12:
            return (str(val)+":"+str(s1[1])+":"+str(s1[2].replace("PM","")))
        val = val +12
        if val>=24:
            val = val%24
            val1 = str(0)+str(val)
            val = str(val1)
        return (str(val)+":"+str(s1[1])+":"+str(s1[2].replace("PM","")))
    elif s.find("PM") ==-1:
        if val == 12:
            val = val%12
            val1 = str(0)+str(val)
            val = str(val1)
        elif val<12:
            val1 = str(0)+str(val)
            val=(str(val1))
        return (str(val)+":"+str(s1[1])+":"+str(s1[2].replace("AM","")))
        
s = input().strip()
result = timeConversion(s)
print(result)
