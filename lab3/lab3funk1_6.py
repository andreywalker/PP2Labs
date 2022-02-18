def rev(ss):
	s_out=""
	for i in range(len(ss.split())-1, -1, -1):
		s_out+=ss.split()[i]
		s_out+=" "
	return s_out
print(rev(input()))