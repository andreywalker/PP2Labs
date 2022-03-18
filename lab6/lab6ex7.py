import os
p=input()
print(os.path.exists(p))
print(os.path.exists(p[0:4]))
print(os.access(p, os.R_OK))
print(os.access(p, os.W_OK))
print(os.access(p, os.EX_OK))
