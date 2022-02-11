d=input()
x0=int(d.split()[0])
y0=int(d.split()[1])
n=int(input())
a=[]
for i in range(0, n):
    s=input()
    a.append(  ((  int(s.split()[0]), int(s.split()[1])), ((int(s.split()[0])-x0)**2+(int(s.split()[1])-y0)**2)**0.5   )   )
asort=sorted(a, key=lambda p: p[1])
for i in asort:
    print(str(i[0][0])+" "+str(i[0][1]))