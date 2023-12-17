'''def hello_world():
    for i in range(4):
        print('hello,world!')
        
hello_world()
'''
'''
def hello(name):
    return f"hello,{name}!how are you?"
    
result=hello("ram")
print(result)
'''
'''
def person(name,age,address):
    print(f"""
          Hello my name is {name}
          and my age is {age}
          and i live in {address}
          """
          )
    
person(name="ram",age=30,address="satdobato")
'''

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b==0:
        print("error")
    else:
       return(a/b)
a=int(input('enter a number'))
b=int(input('enter second number'))
opr=input('enter any operator')
if opr =="+":
     print(add(a,b))
elif opr=="-":
    print(sub(a,b))
elif opr=="*":
    print(multiply(a,b))
elif opr=="/":
     print(divide(a,b))
else:
    exit


