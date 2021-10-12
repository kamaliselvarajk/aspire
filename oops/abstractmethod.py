from abc import ABC, abstractmethod
class Computer(ABC):              
    @abstractmethod
    def process(self):                  
        pass

class Desktop(Computer):  
    def process(self):                  
        print('Desktop')

class Laptop(Computer):  
    def process(self, com):                  
        print('Laptop')
        com.process()

lap = Laptop()
desk = Desktop()
lap.process(desk)          
