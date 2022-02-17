class Shape:
	def __init__(self,  lenght):
		self.lenght=lenght
		self.areav=0
	def getArea(self):
		return(self.areav)
	def getLenght(self):
		return(self.lenght)
	def area(self):
		print(self.areav)
class Square(Shape):
	def __init__(self, lenght):
		super().__init__(lenght)
		self.areav=lenght**2

class Rectangle(Shape):
	def __init__(self, lenght, width):
		super().__init__(lenght)
		self.width=width
		self.areav=self.lenght*self.width

#проверка работы подклассов и наследованых функций
n=int(input()) #5

sq1=Square(n)
print(sq1.getArea())  #25
sq1.area()   #25
l=int(input())   #2
w=int(input())   #3
rect=Rectangle(l,w)
print(rect.getArea())   #6