# def square(a):#we are wasting lines of code
#     return a*a
#
# result = square(5)
# print(result)
#
# v =lambda n : n*n
# r2 =v(9)
# print(r2)
# n = lambda a,b : a+b   #you can [ass any number of arguments but it should on one expression eg:a*a a*b
# t4 = n(5,2)
# print(t4)

######part 2 filter(), map(),  reduce()
# def is_even(n):
#     return n%2==0
#
#
#
#
#
# num = [43,34,35,24,1,324,53,535,5,3]
# even = list(filter(is_even,num))#in filter = 1st fun  and iterated
# print(even)
#
# number =[3,21,23,42,56,4,456]
# evens = list(filter(lambda n : n%2==0,number))
# print(evens)
##map
from functools import reduce
n1 = [83,645,3,4,346,34,3,53]
even1 = list(filter(lambda n:n%2==0,n1))

double = list(map(lambda n : n*2,even1)) # we can add sub multi int his map
def add_all(a,b):
    return a+b


sum  =reduce(add_all,double) #this or
s1 = reduce(lambda a,b:a+b,double)#this #reduce takes two val on is function  and the itreater which is stroed in a variable
print(s1)
print(sum)
print(double)

print(even1)
#we can use lambda instead of def function


