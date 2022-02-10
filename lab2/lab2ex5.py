s=input().split()
if len(s)==2:
    n=int(s[0])
    x=int(s[1])
elif len(s)==1:
    n=int(s[0])
    x=int(input())
a=x
for i in range(1, n):
	a^=x+2*i
print(a)