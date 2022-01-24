# def add(a,b):#now this is formal argument and it has four types
#     c = a + b#that is position ,keyword,default,variablr length
#     print(c)
#
# add(4,8)#when we call it it become a actual argument
def person(name,age):#now this is position #we need not maintain a sequence
    print(name)
    print(age)
person('jone',19)#when we use key words there will be no error in position
person(age = 19,name = 'jone')
###default
def fb(userid,age = 18):#we are assigning the value of age to be default
    print(userid)#and when the user chage the age the program will rewrite the no issue
    print(age)

fb('jone')
fb("andrew",44)
##valriable length
def sum(a, *b):#what if we want to add multiple values we can assign 1 to a and multiple values to b
    c = a
    for i in b:
        c = c +i #by this *b
    print(c)

sum(3,5,43,2,32,3)
#or u can do this way
def sum1(*b):#what if we want to add multiple values we can assign 1 to a and multiple values to b
    c = 0
    for i in b:
        c = c +i #by this *b
    print(c)

sum1(5,43,2,4,5,4)

##contine functions(keyword length arguments)
def person2(name,**data):#if we are using multiple data without keyword we use this
    print(name)
    print(data)


person2('jone andrew',age = 23, city='tamil nadu',mob =  9787898034)
def person3(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)
person3('harris', age = 45, city = 'tirupur', mob_no = 9943398034)