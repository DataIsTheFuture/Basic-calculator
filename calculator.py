from subpackage.addition import * 
from subpackage.subtraction import *
from subpackage.multiplication import *
from subpackage.division import *

x = float(input('Write a number: '))
z = input('Write an operator: ')

while z != '-' and z != '+' and z != '*' and z != '/':
        print('This is not an operator!')
        z = input('Try again: ')

y = float(input('Write a number: '))

if z == '-':
        subtraction(x,y)
elif z == '+':
        addition(x,y)
elif z == '*':
        multiplication(x,y)
elif z == '/':
        division(x,y)
        
print ('Have a good day, Patricia! :)')
    