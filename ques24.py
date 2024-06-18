a=int(input('enter first number'))
operand=input('enter operation')
b=int(input('enter second number'))
if(operand=='+'):
    print(a+b)
elif(operand=='-'):
    print(a-b)
elif(operand=='/'):
    print(a/b)
elif(operand=='*'):
    print(a*b)
else:
    print('enter valid operation')