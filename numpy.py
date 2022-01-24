from numpy import *

# arr  =array(([1,3,4,7.9],[1,5,8,7]))
# print(arr.dtype)
#in the below function we can spilt these
# x = linspace(1,20)
# print(x)
# c = arange(1,20,3)#the multile of 3 will not be displayed
# print(c)
# i = logspace(1,15)
# # print('%.2fi'%i[4])
# c =zeros(((2,2,2)))
#
# print(c)
# v =ones((4,4),int)
# # print(v)
# c = array([1,2,3,4,5])
# n =array([6,7,4,9,8])
# # c = c +5
# print(c)
# print(log(c))
# print(sqrt(c))
# v =c + n
# print(v)
# print(concatenate([c,n]))

###coping arrays
#two types #shllow copy # deep copy
# b = c.view()#the view will create a unique address eventhoung th values are same
# c[1]=7
# print(b)
# print(c)
# print(id(c))
# print(id(b))
# if we change the value in either of them it will change id this is shallow copy
#in deep copy the value does nt match
# b = c.copy()#the view will create a unique address eventhoung th values are same
# c[1]=7
# print(b)
# print(c)
# print(id(c))
# print(id(b))
#dimentionss
# t = array([[[5,6,8,8],
#           [7,8,4,3],
#           [6,2,1,5]]])
#
# print(t.ndim)
# print(t.flatten())#now it is one dimentional
# print(t.reshape(4,3))
# #when we use matrix it will capable of doing more stuffs
# v = matrix(t)
# print((v))#the result will be same
#in martrix we no need to seprate rows with bracts
b = matrix('1 2 3 ; 3 2 1 ; 4 6 3')
n = matrix('3 2 1 ; 1 2 3 ; 5 8 3')
# print(b)
# print(diagonal(b))
j = b * n;
print(j)