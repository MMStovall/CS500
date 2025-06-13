#!/usr/bin/env python3


#catches invalid inputs
while True:
    try:
      num_books_purchased = int(input('please enter the number of books purchased this month\n')) 
      if num_books_purchased < 0:
        num_books_purchased = int(input('Input is invalid please enter number of books again\n'))
      break #valid input,exit loop
    except ValueError:
        num_books_purchased = int(input('Input is invalid please enter number of books again\n'))


  
#functions to find the number of points  
def findPurchasePoints(books):
    
    if books >=2 and books < 4:
        purchase_points = 5
    elif books >= 4 and books < 6:
        purchase_points = 15
    elif books >= 6 and books < 8:
        purchase_points = 30
    elif books >= 8:
        purchase_points = 60
    else: 
        purchase_points = 0         
    return purchase_points
    

#function call   
points = findPurchasePoints(num_books_purchased)
#outputs
print('\nPoints Summary')
print('Customer was awarded {} of points for purchasing {} books'.format(points,num_books_purchased))    
    
    
