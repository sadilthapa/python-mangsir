def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    try:
        if b==0:
            raise Exception('cannot divide by 0')
        else:
            return(a/b)
    except Exception as e:
        print(e)
        