# -*- coding: utf-8 -*-
"""
A program to calculate the tax owed based on the income, dependents, and the mortgage interest.

@author: Sackitey Joseph

"""

# Declaring variables to receive input from the user
currency= "$"

income_amount= int(input("Enter your income: "))

number_of_dependants = int(input("Enter the number of dependants: "))

mortgage_interest= int(input("What's the mortgage interest:  "))

# this is to store the tax benefit of each dependant
benefit = 5000
# This is the value after the dependants benefit is deducted(Used to determine the tax brackect)
adjusted_income= income_amount-(benefit*number_of_dependants)

#Deductions stores the value for total deductions,i.e mortgage interest plus dependant benefit

deduction= (benefit*number_of_dependants) + (mortgage_interest)

#Taxable income is the amount to be taxed in each tax bracket
taxable_income= income_amount- deduction

# Initialize the initial tax value
tax_owed=0
tax_rate= 0
# Using conditionals to calculate the tax of each tax bracket
#Taxable income less than $40000
if adjusted_income < 40000:
    tax_rate= 0
#Taxable income between $40000 and $75000    
elif adjusted_income < 75000:
    tax_rate= 0.2
    
# Taxable income between $75000 and $100000, deductions does not include mortgage interest  
elif adjusted_income < 100000:
    tax_rate= 0.25
    taxable_income = adjusted_income
    
 # No deductions were made,tax calculation based on original income   
else:
    tax_rate = 0.25
    taxable_income = income_amount
    
    
tax_owed= tax_rate*taxable_income 
   
print(f"\t For an income of {currency}{income_amount:,.2f}")
print(f"\t With {number_of_dependants} dependants")
print(f"\t Adjusted income:{currency}{taxable_income:,.2f}")
print(f"\t Tax owed is:{currency}{tax_owed:,.2f}")    
    
    
        





