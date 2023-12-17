class Person:
    name='shyam'
    occupation='shopkeeper'
    Networth=30000
    
    def info(self):
       print(f"{self.name} is a {self.occupation}")
       
a=Person()
b=Person()
c=Person()
a.name='Hari'
b.name='om'
c.name='trick'
a.occupation='accountant'

a.info()
b.info()
c.info()

             