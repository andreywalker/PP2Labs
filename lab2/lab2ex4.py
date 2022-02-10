n=int(input())
if n%2==1:
	for i in range(0,n):
		s="."*(n-i-1)
		s+="#"*(i+1)
		print(s)		
elif n%2==0:
	for i in range(0,n):
		s="#"*(i+1)
		s+="."*(n-i-1)
		print(s)	