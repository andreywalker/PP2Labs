import math

#1

n=int(input())
g=(x**2 for x in range(1,n))
for a in g:
	print(a)

#2

print("2 задачка")

n=int(input())
g=(2*x for x in range(1,int(math.ceil(n/2))))
s=""
for a in g:
	s+=str(a)
	s+=", "
s=s[0:len(s)-2]
print(s)

#3

print("3 задачка")

def divisible_by_3_or_4(d, n):
	if d!=4 and d!=3:
		print("там либо тройка либо четверка должна быть")
		return 0
	elif d==4:
		g=(x*4 for x in range(0,math.ceil(n/4)))
		return g
	else:
		g=(x*3 for x in range(0,math.ceil(n/3)))
		return g

print("на 3:")
n= int (input())
for a in divisible_by_3_or_4(3,n):
	print(a)
print("на 4:")
for i in  divisible_by_3_or_4(4,n):
	print(i)

#4

print("4 задачка")

a=int(input())
b=int(input())
squares=(x**2 for x in range (a,b))
for i in squares:
	print(i)


#5

print("5 задачка")

n=int(input())
u=(x for x in range(n,0,-1))
for i in u:
	print(i)
