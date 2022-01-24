app_name = input('enter your name: ')
skills_known =input("skill known : ")
age = int(input('age: '))
experience = int(input('experience: '))
if skills_known == 'data science'or'meachine learning' or 'deep learning':
    print('ur in')
else:
    print('not  eligible')
if age>30:
    print('age limit acrossed')
else:
    print('ready to get in')
if experience<5:
    print('meet me after this')
