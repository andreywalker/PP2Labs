a=[]
b=[]
n=int(input())
for i in range(0,n):
	s=input()
	if s[0]=="1":
		a.append(s.split()[1])
	else:
		b.append(a[0])
		a.pop(0)
h=""
for i in b:
	h+=i+" "
print(h)