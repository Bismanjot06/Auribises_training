#factorial: 5*4*3*2*1

def factorial(number):
    if number==0:
        print('invalid number')
    else:
     number = factorial(number-1)
     return
result= factorial(number=5)
print('result',result)