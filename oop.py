import csv


class applicant:
    pay_rate = 500
    all =[]
    def __init__(self,name:str, age:int, experience=1):
        #assert is run validation to the recieved aurguments
        assert age >=18,f'{age} is not eligiable sorry'
        assert experience>=0,f'the{experience} is not greater than 0'
        self.name = name
        self.age = age
        self.experience = experience
        # actions to execute
        applicant.all.append(self)

    def form(self):
        print(f'applicant name: {self.name}')
        print(f'applicant age {self.age}')
        if self.experience!=0:
            print('eligible')
        else:
            print('not eligible')
    def pay_emp(self):
        self.experience = self.experience * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        with open('applicants.csv','r') as f:
            reader = csv.DictReader(f)
            applicants=list(reader)
        for item in applicants:
            applicant(
                    name=item.get('name'),
                    age=int(item.get('age')),
                    experience=int(item.get('experience')),
            )
    def __repr__(self):# decode the object to actually str in the output
        return f"applicant('{self.name}',{self.experience},{self.age})"


applicant.instantiate_from_csv()
print(applicant.all)




#7 applicant1 =applicant('jone',22,0)
#7 applicant2 =applicant('andrew',34,8)
#7 applicant3 =applicant('harris',23,2)
#7 applicant4 =applicant('x',31,7)
#7 applicant5 =applicant('y',28,6)
#8 print(applicant.all)
#6 for i in applicant.all:
#6     print(i.name)
# print(applicant1)

# print(apllicant2)
# print(applicant1.form())
# print(apllicant2.form())
## print(applicant.pay_rate)
##print(applicant1.pay_rate)
## print(applicant2.pay_rate)
### print(applicant.__dict__)# for checking
### print(applicant1.__dict__)# for checking that why the payrate variable is printing
#### applicant2.pay_emp()
#### print(applicant2.experience)
##### applicant2.pay_rate = 3000
##### applicant2.pay_emp()
##### print(applicant2.experience)
#inside a class  attibutes == variables
#and behaviour ==  methods or function


















