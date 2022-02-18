def filter_prime(a):
	b=[]
	for ai in a:
		not_prime=False
		for i in range(2,int(ai/2+1)):
			if ai%i==0:
				not_prime=True
		if  not not_prime or ai==1 or ai==2:
			b.append(ai)
	return b
ss=input().split()
a=[]
for s in ss:
	a.append(int(s))
print(filter_prime(a))
