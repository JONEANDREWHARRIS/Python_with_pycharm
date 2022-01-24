class Computer:
    def process(self):
       pass #if pass is mentioned then it a Abstract method #body of methond
# in python if we want an abstract cls wee need to import this
from abc import ABC,abstractmethod
class Computer1(ABC):
    @abstractmethod
    def process(self):#we cant store abstract cls in a variable like this comp = Computer1() , com.process()
        pass
class laptop(Computer1):#now this is an sub class of comp1
    def process(self):
        print('its running')
#if we command comp1 = laptop() it will not run because this (with a pass statement)

comp1 =laptop()
comp1.process()#it is only very use ful when we building