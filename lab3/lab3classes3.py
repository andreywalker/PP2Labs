import math
class Point:
	def __init__(self, x, y):
		self.x=x
		self.y=y
	def show(self):
		return (self.x, self.y)
	def moveTo(self, x, y):
		self.x=x
		self.y=y
	def dist(self, x1, y1):
		d=math.sqrt((x1-self.x)**2+(y1-self.y)**2)
		return d

x=2
y=3
x1=6
y1=17
p=Point(x, y) 
print(p.show())      #2, 3
print(p.dist(x1, y1))#14.56...
p.moveTo(x1, y1)	 
print(p.show())		 #6, 17
