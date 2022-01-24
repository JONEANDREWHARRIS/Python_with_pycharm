#Methods - instance,class,static
class Student:
    school = 'jone school'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 +self.m2+self.m3/2)
    @classmethod#to mention that it is a class method
    def info(cls):#if ur using a class variable we use cls
        return cls.school
    def get_m1(self):#accessor
        return self.m1#mutator
    def set_m1(self,value):
        self.m1 =value
    @staticmethod
    def info():#this is a static method it does not belong to any specitfic catogary
        print('this is for doing some simple random funtion/operation like factorial')

s1 = Student(32,13,12)
s2 = Student(86,67,65)
print(s2.avg())

#in instance method there are two type
#accessor Methods - if u want to fetch the value
#mutator Methods - if u want to modify the value

Student.info()#this works when we us @cclass method in the code by mentioning that it is a class
Student.info()




