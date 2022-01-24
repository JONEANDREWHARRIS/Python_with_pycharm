class Student:
    def __init__(self,name,roll_no):
        self.name =  name
        self.roll_no = roll_no
        self.lap =self.laptop()#if u dont us () the two value will be on the same address
    def show(self):
        print(self.name,self.roll_no)
        self.laptop.show()

    class laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1 = Student('naveen',2)
s2 = Student('jone',4)
print(s1.name,s2.roll_no)
s1.show()
# lap1 =s1.lap
# lap2 =s2.lap
# print(id(lap2))
# print(id(lap1))


