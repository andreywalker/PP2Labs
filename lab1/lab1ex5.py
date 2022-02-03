import cmath
s=input().split()
n=int(s[0])
f=int(s[1])
def is_prime(a):
	isp=True
	for i in range(2,int(a/2)):
		if a%i==0:
			isp =False
		#print(i)
	return isp
if (is_prime(n) and f%2==0 and n<=500):
	print ("Good job!")
else:
	print ("Try next time!")

