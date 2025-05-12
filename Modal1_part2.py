#!/usr/bin/env python3

#getting inputs from user
def getNumbers():
    global num1 
    num1 = int(input('Please enter a number: '))
    global num2 
    num2 = int(input('Please enter a second number: '))

#function to multiply the two numbers gotten from the user
def multiplyNumbers(num1,num2):
    return num1 * num2   
    
#function to divide the two numbers gotten from the user
def divideNumber(num1,num2):
    return num1 / num2 

getNumbers()
print('When you multiply', num1,'and', num2, 'you get',multiplyNumbers(num1,num2))
print('When you divide', num1,'and', num2, 'you get',divideNumber(num1,num2))


