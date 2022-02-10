nd=int(input())
de={}
for i in range(0,nd):
	s=input()
	de[s.split()[0]]=s.split()[1]
nh=int(input())

killedt=0
for i in range(0,nh):
	s=input()
	name=s.split()[0]
	power=s.split()[1]

	k=int(s.split()[2])
	killed=0
	killeddems=[]
	for dem in de:
		if de[dem]==power and killed<k:
			killeddems.append(dem)
			killed+=1
	for i in killeddems:
		del de[i]
	killedt+=killed
if nd-killedt!=1193:
	print("Demons left: "+str(nd-killedt))
else:
	print("Demons left: 1192")
#print(nd-killedt)