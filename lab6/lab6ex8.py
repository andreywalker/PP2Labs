import os
p=input()
if os.path.exists(p):
    print(os.path.basename())
