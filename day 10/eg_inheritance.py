class Grandfather:
    Land='5 Ropani'
    
class Grandmother:
    House='3 Houses'
    
class Father(Grandfather,Grandmother):
    Car='Bentley,Range rover'
    
class Son(Father):
    Bike='KTM'
    
father=Father()
print(father.House)
son=Son()
print(son.Car)