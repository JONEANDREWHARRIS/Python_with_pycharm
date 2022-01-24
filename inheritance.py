class A:
    def feature1(self):
        print('this is feature 1')

    def feature2(self):
        print('feature 2')
class B ():#in B(A) means that b is inheriting the a with funtion and the features including in that
    def feature3(self):
        print('feature 3 is this')
    def feature4(self):
        print('feature 4 is this')

class C(A,B):#multiple features#or u can use single inheritace
    def feature5(self):
        print('thiis is feature 5')
a1 =A()

a1.feature1()
a1.feature2()
b1 = B()