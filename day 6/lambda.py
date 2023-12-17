"""def sum_by_10(a):
    return a+10

    
s=lambda a:a+10
  
print(s(10))
"""
"""
def myfuc(n):
    return lambda x:x*n
doubler=myfuc(2)
print(doubler(10))
    """
    
def myfuc(n):
    return lambda x:x*n
tripler=myfuc(3)
print(tripler(10))