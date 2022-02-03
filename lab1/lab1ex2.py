n=input()
a=0
for c in n:
    a+=ord(c)
if a>300:
    print("It is tasty!")
else:
    print("Oh, no!")
