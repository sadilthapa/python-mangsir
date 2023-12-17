'''
def star(func):
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    return wrapper


def hello():
    print('hello')
    
    
star(hello)()
'''

def hash(func):
    def wrapper():
        print('#'*10)
        func()
        print('#'*10)
    return wrapper

def star(func):
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    return wrapper

def world():
    print("world")
        
hash(star(world))()