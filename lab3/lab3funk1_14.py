import lab3funk1_11

def palindrome(s):
    if s==lab3funk1_11.rev(s):
        return True
    else:
        return False
#print(rev("madam"))
print(palindrome("madam"))
