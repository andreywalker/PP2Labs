def solve(numheads, numlegs):
	n=numheads
	c=0
	for chick in range(0, n):
		if chick*2+(n-chick)*4==numlegs:
			c=chick
	s="You have "+str(c)+" chickens, and "+str(n-c)+" rabbits"
	return s
heads=int(input())
legs=int(input())
print(solve(heads, legs))