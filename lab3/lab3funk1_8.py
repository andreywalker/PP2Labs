def spy_game(a):
	b=False
	for i in range(0,len(a)-2):
		if a[i]==0 and a[i+1]==0 and a[i+2]==7:
			b= True
	if len(a)>2:
		return b
	else:
		return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
