s=input()
a=0
for i in range(0, len(s)):
	a+=int(s[len(s)-i-1])*(2**i)
print(a)

