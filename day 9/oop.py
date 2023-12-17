class house:
    window=1
    door=1
    colour='red'
    
    def __init__(self,window=1,door=2,colour='red',price=1):
        self.price=price
        self.window=window
        self.door=door
        self.colour=colour   
    
    def set_colour(self,colour):
        self.colour=colour
    
    def get_colour(self):
        return self.colour 
    
    
    def __eq__(self,value):
        return self.window==value.window
    
    def __gt__(self,value):
        return self.price>value.price
        
       
ram_ko_ghar=house()
shyam_ko_ghar=house(window=12,colour='black',price=1)
ram_ko_ghar.set_colour('blue')



print(ram_ko_ghar.get_colour())
#print(ram_ko_ghar.door)
#print(ram_ko_ghar.window)
print(shyam_ko_ghar.get_colour())
print(ram_ko_ghar.__eq__(shyam_ko_ghar))
print(ram_ko_ghar.__gt__(shyam_ko_ghar))
