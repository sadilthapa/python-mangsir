class person:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person('Shyam','Shokeeper')
b=person('Hari','HR')
a.info()
b.info()