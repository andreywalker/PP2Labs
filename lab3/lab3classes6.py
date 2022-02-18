import lab3funk1_4
ss=input().split()
a=[]
for s in ss:
	a.append(int(s))
print(lambda a:lab3funk1_4.filter_prime(a))

