s=input()
t=input()
ap=False
a=0
b=0
for i in range (0, len(s)):
    if s[i]==t and not ap:
        a=i
        ap=True
    elif s[i]==t and ap:
        b=i
if ap and b!=0:
    print(a, b)
elif ap and b==0:
    print(a)

