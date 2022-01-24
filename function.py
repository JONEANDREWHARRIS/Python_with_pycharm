# def the_man(x, y):
#     v =x + y
#     r = x *y
#     return v,r
# reslut1,resuslt2 = the_man(9 ,3)
# print(reslut1,resuslt2)


##funtion argumentss
# def updates(x):
#     x =1
#     print('x',x)
# a =10
# updates(10)
# print('a', a)
##general concept
#pass by reference # when we change the value it will effect the value of the changed value
#pass by value
def updates(ist):
    print(id(ist))
    ist[1] = 32
    print(id(ist))
    print('x',ist)

ist = [13,44,22,44]
print(id(ist))
updates(ist)
print('ist', ist)