## acuste opp
the_acuste = input("name :  ")
age = int(input('age: '))
type_of_the_crime = input('what crime did he/she has done: ')

if age <18:
    print('he/she is a minor')
    if type_of_the_crime=='klled':
        print('5 years of cetence')
    elif type_of_the_crime=='theft':
        print('3 years of centence')
    elif type_of_the_crime=='none':
        print('set free')
    else:
        print('fine of 3000$ to 9000$ ')

elif age>18:
    print('he/she is a major')
    if type_of_the_crime =='killed':
        print('centence to death')
    elif type_of_the_crime=='theft':
        print('10 years of centence')
    elif type_of_the_crime=='none':
        print('set free')

    else:
        print('20000$ fine or 4 years of jail')



