s=input()
s=s.replace("."," ")
s=s.replace(","," ")
s=s.replace("!"," ")
s=s.replace("?"," ")
s=s.replace("-"," ")
s=s.replace(":"," ")
ss= s.split()
ss2=[]
for si in ss:
    if si not in ss2:
        ss2.append(si)
ss2.sort()
print(len(ss2))
for si in ss2:
    print(si)