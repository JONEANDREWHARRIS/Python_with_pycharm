# a = 10
#
# def v1():
#     a = 15
#     b = 8
#     print('in fun',a)
#
#
# v1()
# print('outside', a)
#as i know the variable will if we change the 'a' inside the funtion so if we want to mention the program to use gobal vaariable
#we do this
a = 10#this is a global variable

# def v1():
#     global a #but in this we cannot re assaign the same value that is a again and convert it into a local variable
#     a = 15
#     b = 8
#     print('in fun',a)
#
#
# v1()
# print('outside', a)
g  =10
r = 30
e = 40
print(id(g))
def innervarialble():
    g =33

    x = globals()['g']#this how we can use a global and a local value in the function
    print(id(x))
    print('fun in', g)
    globals()['g'] = 44

innervarialble()
print('outside',g)

