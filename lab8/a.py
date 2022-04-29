import math
def f(x):
    y=0.005347*(-((x*0.001-0.0235)/pow(0.000068+(x*0.001-0.0235)**2,0.5))+((x*0.001+0.0235)/pow((0.000068)+(x*0.001+0.0235)**2,0.5)))
    return y
b=[]
b.append(0.27)
b.append(0.64)
b.append(0.9)
b.append(0.98)
b.append(1.02)
b.append(1.01)
b.append(1.02)
b.append(0.98)
b.append(0.82)
b.append(0.37)
b.append(0.13)
for i in range(-25,26,5):
    print (str(i)+"   "+str(f(i))+"    "+str(0.01*b[int((i/5)+5)])+"    "+str((f(i)-0.01*b[int((i/5)+5)])/f(i))+"    ")
