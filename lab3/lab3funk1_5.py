from itertools import permutations
def perms(s):
	return(list(permutations(s)))
s=input()
ss=perms(s)
for ai in ss:
	si=""
	for aii in ai:
		si+=str(aii)
	print(si)