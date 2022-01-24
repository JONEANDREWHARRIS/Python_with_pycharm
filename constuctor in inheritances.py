#using features of existing class

# MRO (Method Resolution order)

class A:#super cls
    def __init__(self):
        print('in a init')
    def feature1(self):
        print('this is feature 1')

    def feature2(self):
        print('feature 2')
class B (A):
    def __init__(self):#when u call a sub cls it will call init of sub cls first
        super().__init__()#and then use this to acess the init of a
        print('init b')#in B(A) means that b is inheriting the a with funtion and the features including in that
    def feature3(self):#b is a sub cls #sub cls can acess all feature of super cls but not vise versa
        print('feature 3 is this')
    def feature4(self):
        print('feature 4 is this')
a1= A()
a2 =B()