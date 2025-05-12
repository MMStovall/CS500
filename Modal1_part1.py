#!/usr/bin/env python3

#getting inputs from user
def getNumbers():
    global num1 
    num1 = int(input('Please enter a number: '))
    global num2 
    num2 = int(input('Please enter a second number: '))

#function to add the two numbers gotten from the user
def addNumbers(num1,num2):
    return num1 + num2   
    
#function to subtract the two numbers gotten from the user
def subtractNumber(num1,num2):
    return num1 - num2 

getNumbers()
print('When you add', num1,'and', num2, 'you get',addNumbers(num1,num2))
print('When you subtract', num1,'and', num2, 'you get',subtractNumber(num1,num2))



