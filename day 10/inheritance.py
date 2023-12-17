class Grandfather:
    house='Luxury house'
    def get_house(self):
        return self.house
    
    
class Grandmother:
    jewelery='Diamond'
    
class Father(Grandfather,Grandmother):
    car='lexus'
    def get_house(self):
        print(super().get_house())
        return "Mansion"   
       
class son(Father):
    console='Playstation'
    
    
father=Father()
print(father.get_house())
#print(isinstance(son,Grandfather))

#task
#make another inheritance

