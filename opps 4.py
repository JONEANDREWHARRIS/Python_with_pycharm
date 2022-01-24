#variable are two types
# instance , class variables
class Car:#if u create a variable in ouside init it becomes a class(inside class) variable
    wheels = 4#comman variables

    def __init__(self):# if you create a variable inside a init it become an instant variable
        self.mil = 10
        self.comp = 'BMW'
c1 = Car()
c2 = Car()
c2.mil =15
print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)
##in a memory we have different namespace
#name space is a area where you create and store object and variable
#two types class or static and object or instance





