
#1

print("1task")

a=list(map(int,input().split()))
p=1
for i in range(0,len(a)):
    p*=a[i]
print(p)
