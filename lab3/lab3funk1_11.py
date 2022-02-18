def rev(ss):
	s_out=""
	for i in range(len(ss)-1, -1, -1):
		s_out+=ss[i]
	return(s_out[0:len(ss)])

def palindrome(s):
    if s==rev(s):
        return True
    else:
        return False
#print(rev("madam"))
print(palindrome("madam"))
