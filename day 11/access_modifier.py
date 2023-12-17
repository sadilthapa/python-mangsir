class Person:
    def __init__(self,name,age,password):
        self.name=name
        self._age=age
        self.__password=password
        
    @property   
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password
        
    

  
person=Person("ram",12,"hello")    
print(person.name)
print(person._age)
#person.set_password('123')
print(person.password)    
#person.password=123
#print(person.password)