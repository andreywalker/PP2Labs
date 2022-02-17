class BankAccount:
	def __init__(self, owner):
		self.owner=owner
		self.balance=0
	def deposit(self,n):
		self.balance+=n
		s="текущий счет составляет "
		s+=str(self.balance)
		print(s)
	def withdraw(self,n):
		if n>self.balance:
			print("недостаточно средств")
		else:
			self.balance-=n
			s="текущий счет составляет "
			s+=str(self.balance)
			print(s)

vasin_akk=BankAccount("Vasya")
vasin_akk.deposit(31000)
vasin_akk.withdraw(120)
vasin_akk.withdraw(100000)

