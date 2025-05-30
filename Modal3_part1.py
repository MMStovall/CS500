#!/usr/bin/env python3

sales_tax = .07
tip = .18
foodSubTotal = float(input('Please enter your Meal Total\n'))
totalSalesTax = 0
totalTip = 0 
finalAmount = foodSubTotal

    
#function finding total sales tax
def salesTaxTotal(foodPrice,sales_tax):
    return foodPrice * sales_tax 
    
totalSalesTax = salesTaxTotal(foodSubTotal,sales_tax)
finalAmount += totalSalesTax   
 
#function finding total of tip
def tipTotal(foodPrice,tip):
    return foodPrice * tip


totalTip = tipTotal(finalAmount,tip)
finalAmount += totalTip


print('RECEIPT\n')
print('Meal  subtotal:  ${:.2f}\n'.format(foodSubTotal))
print('           Tax:  ${:.2f}\n'.format(totalSalesTax))
print('           Tip:  ${:.2f}\n'.format(totalTip))
print('         Total:  ${:.2f}\n'.format(finalAmount))


