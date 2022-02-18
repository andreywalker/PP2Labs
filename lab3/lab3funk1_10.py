def uniq(a):
	b={}
	o=[]
	for ai in a:
		b[ai]=0
	for x in b:
		o.append(x)
	return(o)
print(uniq(input().split()))

