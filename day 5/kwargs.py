'''
def person(**kwargs):
    print(kwargs)
    
person(name='ram',age=15)
'''

#task
#add more attribute and print in proper string
 
 
def person(**kwargs):
    print(f"My name is {kwargs['name']}")
    print(f"My age is {kwargs['age']} years old")
    print(f"I live in {kwargs['address']}")
    print(f"My sex is {kwargs['sex']}")
   
person(name="Sadil",age=19,address="jawalakhel",sex="male")


