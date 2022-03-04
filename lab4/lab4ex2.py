import math

#1

a=int(input())
print(math.radians(a))

#2

h=int(input())
b1=int(input())
b2=int(input())
s=(math.fabs(b1+b2)/2)*h
print(s)

#3

n = int(input())
a= int(input())
R=a/(2*math.sin(math.pi/n))
r=R*math.cos(math.pi/n)
p=n*a
s=p*r/2
print(s)

#4

h=int(input())
a=int(input())
s=a*h
print(s)
