import re

#1

print("1 task")

s="The capital of great britain is london. Not friggin milan. It is in spain"
print(type(re.search(".a*b", s))!=type(None))

#2

print("2 task")

s="The capital of great britain is london. Not friggin milan. It is in spain"
print(type(re.search("ab+", s))!=type(None))

#3

print("3 task")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE)"
print(re.findall("[a-z]+_[a-z]+", s))

#4

print("4 task")

s="The capital of great britain is london. Not friggin milan. It is in spain. Let's make some snake_case here. What a hell?! Who even uses it?! Nobody! Men prefer CamelCase. (Don't even mention kebab-case. Don't. It will cause only EMOTIONAL DAMAGE)"
print(re.findall("[A-Z]{1}[a-z]+", s))