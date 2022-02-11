s=input()
sb=0
fb=0
b=0
for i in s:
	if i=="(":
		b+=1
	elif i==")":
		b-=1
	elif i=="[":
		sb+=1
	elif i=="]":
		sb-=1
	elif i=="{":
		fb+=1
	elif i=="}":
		fb-=1
	
if sb==0 and fb==0 and b==0 and (s[0]=="(" or s[0]=="[" or s[0]=="{"):
	print("Yes")
else:
	print("No")