'''

Task 5 - Capstone Project
Prepare a program for a small financial company to access two financial calculators
The following code calculates an investment or a bond repayment


'''


# Import math Library.
import math


                    
#                                                                                                *** CAPSTONE PROJECT ***


                                                                               
# Asking a user on their choice of the calculator.
# By selecting either investment or bond option. 
calculation_type = input("""Enter either 'investment' or 'bond' from the menu below to proceed:

                            investment    - to calculate the amount of interest you'll earn on interest
                            bond          - to calculate the amount you'll have to pay on a home loan

""")

# Casefold function used to set all characters to lowercase.
# All options are accepted into the conditional statatement.
# For example Bond or bond etc, are accepted.
# Using replace() function to remove any spaces. 
calculation_type = calculation_type.casefold().replace(" ", "")
print("\n" + "=" * 100)  # Print statement added for the better presentation. 


# Find out output actions depending on the calculator chosen.
# Calculation_type is equal to investment.
if calculation_type == "investment":
    
    deposit_value = float(input("\nPlease input the amount of money you wish to deposit:\n"))  # Getting input from user on deposit to insert into investment calculator.                 
    interest_rate = int(input("\nPlease input your interest rate as a number (e.g. 8,9 etc.):\n")) # Getting information from user on interest rate.
    number_years = int(input("\nPlease input the number of years you plan on investing for:\n")) # Getting information from user on years of investing.
    interest = input("\nPlease input your investment choice type: (simple or compound)\n") # Asking a user to choose an investment type.

     
# Formulas for simple and compound interest depending on user choice. 
# Casefold function used to set all input characters to lowercase.
    interest = interest.casefold().replace(" ", "")


    if interest == "simple": # Interest is equal to simple.
        simple_interest = round(deposit_value*(1 + (interest_rate/100)* number_years), 2) # Calculate the simple interest.
        print("\n" + "=" * 100)
        print(f"After {number_years} years of investing at {interest_rate}%,\
 you will earn £{simple_interest}") # Print out the results.
        
        
    elif interest == "compound": # Interest is equal to compound.
        compound_interest = round(deposit_value* math.pow((1 + interest_rate/100), 
                                                                number_years), 2) # Calculate the compound interest.
        print("\n" + "=" * 100)
        print(f"After {number_years} years of investing at {interest_rate}%,\
 you will earn £{compound_interest}")
        
        
# Introducing second part of conditional statement for bond calculator.
# Calculation_type is equal to bond.
elif calculation_type == "bond":      

    house_value = int(input("\nPlease input value of your house:\n")) # Getting input from user on home value.
    interest_rate = int(input("\nPlease input your interest rate as a number (e.g. 5,6 etc.):\n")) # Getting information from user on interest rate.
    num_months = int(input("\nPlease input the number of months you wish to repay the bond:\n")) # Asking a user to declare for how long want to repay for.

    
# Entering formula for bond calculator.  
# Use round function, to round it two decimal places.      
    repayment = round((interest_rate/100/12 * house_value) / 
                      (1 - math.pow((1+ interest_rate/100/12), 
                                      (-1 * num_months))), 2)
    
 
# Print statement added for the better presentation.  
    print("\n" + "=" * 100)
# Displaying monthly payment results.
# Use f-function for formatting purposes.        
    print(f"\nYour monthly repayment amount for the home loan is to £{repayment}\n") 
    
   
# Invalid message display if condition has not been met.   
# Advise for the user to enter 'investment' or 'bond' word to proceed.   
else:
    print("\nInvalid selection. Please enter either 'investment' or 'bond'.\n")




