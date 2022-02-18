def histogram(a):
	for ai in a:
		s=""
		for aii in range(0,ai):
			s+="*"
		print(s)
histogram([1,2,3,5])