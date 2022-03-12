import re

#1

print("1 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain"
print(type(re.search(".a*b", s))!=type(None))

#2

print("\n")
print("2 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain"
print(type(re.search("ab+", s))!=type(None))

#3

print("\n")
print("3 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE)"
print(re.findall("[a-z]+_[a-z]+", s))

#4

print("\n")
print("4 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE)"
print(re.findall("[A-Z]{1}[a-z]+", s))

#5

print("\n")
print("5 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE). Really?! I don't have any word ending with 'b'? it is a FAILURE! Tere are so maby such words: scrab cab cub tub lab pub tab "
# Let' create another string to work with
a="lab"
print(re.findall(".a.*b$", a))

#6

print("\n")
print("6 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE). Really?! I don't have any word ending with 'b'? it is a FAILURE! Tere are so maby such words: scrab cab cub tub lab pub tab "
# Let' create another string to work with
a="lab"
s=re.sub("\s","",s)
s=re.sub("[.]","",s)
s=re.sub(":","",s)
s=re.sub(",","",s)
print(s)

#7

print("\n")
print("7 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case and one_more here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE). Really?! I don't have any word ending with 'b'? it is a FAILURE! Tere are so maby such words: scrab cab cub tub lab pub tab "

i=0
def toCamel(match):
    global i
    g=match.group()[1:]
    c=g[0]
    g=g[1:]
    g=str(c).upper()+g
    i+=1
    return g
s=re.sub("_[a-z]+", toCamel ,s)
print(s)

#8

print("\n")
print("8 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE). Really?! I don't have any word ending with 'b'? it is a FAILURE! Tere are so maby such words: scrab cab cub tub lab pub tab "
ss=re.split("[A-Z]", s)

print(ss)


#9

print("\n")
print("9 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE). Really?! I don't have any word ending with 'b'? it is a FAILURE! Tere are so maby such words: scrab cab cub tub lab pub tab "
i=0
def separateCamel(match):
    global i
    g=match.group()
    c=" "
    g=str(c)+g
    i+=1
    return g
s=re.sub("[A-Z]{1}[a-z]+", separateCamel ,s)

print(s)


#10

print("\n")
print("10 task")
print("\n")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE). Really?! I don't have any word ending with 'b'? it is a FAILURE! Tere are so maby such words: scrab cab cub tub lab pub tab "
i=0
def to_snake(match):
    global i
    g=match.group()
    c=g[len(g)-1]
    g=g[:len(g)-1]+"_"+str(c).lower()
    i+=1
    print(g)
    return g
s=re.sub("[a-z]+[A-Z]{1}", to_snake ,s)

print(s)
