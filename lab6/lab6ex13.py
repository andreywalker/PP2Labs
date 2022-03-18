import os
if os.access("C:\Users\User\Desktop\PP2Labs\lab6\llll.txt", os.EX_OK) and os.path.exists("C:\Users\User\Desktop\PP2Labs\lab6\llll.txt"):
    os.remove("C:\Users\User\Desktop\PP2Labs\lab6\llll.txt")
