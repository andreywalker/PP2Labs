#2

s="dfghRSGDZHagzdshfASFGDZhf"
def isUpper(c):
    if ord(c)>64 and ord(c)<91:
        return True
    else:
        return False
def isLower(c):
    if ord(c)>96 and ord(c)<123:
        return True
    else:
        return False

uppers=len(list(filter(isUpper,s)))
lowers= len(list(filter(isLower, s)))
print(len(s))
print(uppers)
print(lowers)