a=input().split()
for i in range(0, len(a)):
    a[i]=int(a[i])
canBeReached=False
i=0
while i<len(a)-1:
    if a[i]>0 and a[i+a[i]]!=0:
        i+=a[i]
    elif a[i]>0 and a[i+a[i]]==0:
        zeroCanBeAvoided=False
        for j in range(1,a[i]):
            if a[i+a[i]-j]!=0:
                i+=(a[i]-j)
                zeroCanBeAvoided=True
                
            