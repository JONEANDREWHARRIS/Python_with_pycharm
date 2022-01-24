class Computer:#cpu and is an argument if we need it to ne an object we need to assign it to self(object)
	def __init__(self,cpu,ram):
		self.cpu = cpu
		self.ram = ram


	def config(self):
		print('config is',self.cpu,self.ram)

com1 = Computer('i4',16)
com2 = Computer('ryzen 7',8)

com1.config()
com2.config()