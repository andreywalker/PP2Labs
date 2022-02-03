n=float(input())
c=input()
if c=='b':
    n=int(n)
    print(n*1024)
else:
    r=int(input())
    n=round(n/1024,r)

   # n=int(n*(10**r))/(10**r)
    print(n)