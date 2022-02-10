n=int(input())
for i in range(0,n):
	s=""
	for j in range(0,n):
		if i==0:
			s+=str(j)+" "
		elif j==0:
			s+=str(i)+" "
		elif i==j:
			s+=str(i*i)+" "
		else:
			s+=str(0)+" "
	print(s)
