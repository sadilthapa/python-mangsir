'''
while True:
    try:
        
     num1=int(input('enter a number'))
     num2=int(input('enter a number'))
     print(num1/num2)
    except ZeroDivisionError:
        print('cannot divide by 0')
    except Exception as e:
        print('Something went',e)
        '''

def divider():
    num1=int(input('enter a number'))
    num2=int(input('enter a number'))
    if num1==5:
        raise Exception('input number cannot be 5')
    print(num1/num2)
while True:
    try:
        divider()
    except ZeroDivisionError:
        print('cannot divide by 0')
    except Exception as e:
        print('something went',e)