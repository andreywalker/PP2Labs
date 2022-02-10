n=int(input())
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
pr=0
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]*a[j]>pr:
            pr=a[i]*a[j]
print(pr)
