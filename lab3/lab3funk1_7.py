def has_33(a):
	b=False
	for i in range(0,len(a)-1):
		if a[i]==3 and a[i+1]==3:
			b= True
	return b
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

