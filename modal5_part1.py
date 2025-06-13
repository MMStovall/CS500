#!/usr/bin/env python3
#getting user input for number of years
num_years = int(input('Enter number of years to collect rainfall data\n'))

#using a list of Months to tell the user what month they are entering data for
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']

#intiating rainfall total and number of months
rainfall_total = 0 
total_num_months = 0


if num_years > 0: 
    for i in range(0,num_years,1):  #loop though each year
        for j in range(0,12,1): #loop through each month of the year
            rainfall = int(input('how much rain fell in month {} of year {}\n'.format(months[j],i+1)))
            if rainfall > 0:
                rainfall_total +=rainfall 
                total_num_months += 1
            else:
                print('\nRainfall can not be negative')
                rainfall = int(input('\nPlease enter amount of rainfall of this month again\n'))
                total_num_months += 1
                
    #finding the average of rainfall
    average_rainfall = rainfall_total/total_num_months
    
    print("\n--- Rainfall Summary ---")
    print(f"Total months: {total_num_months}")
    print(f"Total rainfall: {rainfall_total:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
else:
    print('\nYou cannot collect data for a negative number of years: Good Bye')
    


