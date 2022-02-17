class Stringmethods:
	def __init__(self, string):
		self.string=string
	def getString(self):
		return (self.string)
	def printString(self):
		print(self.string.upper())
s=Stringmethods(input())
print(s.getString())
