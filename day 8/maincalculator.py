from calculatormodule import *

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