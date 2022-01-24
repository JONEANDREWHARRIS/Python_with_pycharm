class Computer:
    def __init__(self):
        self.name =  'jone'
        self.age = 24

    def compare(self,other):
        if self.age ==other.age:
            return True
        else:
            return False



c1 = Computer()
c2 = Computer()
c2.age = 44
if c1.compare(c2):
    print('they are equal')

else:
    print('none')
print(c1.age)
print(c2.age)# every tume you buid an object or input an obj it will give a different address
#how much space will it take
#it depends upon the variables we have
#and no of variables
