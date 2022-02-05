n=int(input())
for i in range(0, n):
    s=input()
    if s.endswith("@gmail.com"):
        print(s[0:len(s)-10])
