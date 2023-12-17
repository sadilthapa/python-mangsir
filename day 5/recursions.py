'''
def number(num=0):
    print(num)
    number(num+1)
number()
'''
#task
#range()

def range(num):
    if num==0:
        return 0
    else:
        return range(num-1)
range(20)
    



    
    
    