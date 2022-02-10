n=int(input())
di={}


for i in range(0, n):
	s=input()
	if s.split()[0] in di:
		di[s.split()[0]]=int(di[s.split()[0]]+int(s.split()[1]))
	else:
		di[s.split()[0]]=int(s.split()[1])
m=max(di.values())
for hi in di:
	
	if m-di[hi]==0:
		di[hi]=" is lucky!"
	else:
		di[hi]=" has to receive {} tenge".format(m-di[hi])
dis=list(di.keys())
dis.sort()
for i in dis:
	print(i+di[i])
