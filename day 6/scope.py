"""a=10#global scope
def number():
    a=11#local scope
    print(a)
    
number()
print(a)
"""

"""
a=10
def num():
    global a
    a=11
    print(a)
num()
print(a)"""


a=10
def outer():
    a=11
    def inner():
        print("inner sees a as",a)
    inner()
    print('outer sees a as',a)
    
outer()
print('main sees a as',a)