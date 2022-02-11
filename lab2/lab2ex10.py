n=int(input())
ss=[]
for i in range(0, n):
	s=input()
	num=False
	uper=False
	lower=False
	for c in s:
		if ord(c)>47 and ord(c)<58:
			num=True
		elif ord(c)>64 and ord(c)<91:
			uper=True
		elif ord(c)>96 and ord(c)<123:
			lower=True
	if num and uper and lower and s not in ss:
		ss.append(s)
print(len(ss))
ss.sort()
for s in ss:
	print(s)
