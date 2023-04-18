# Write a program to calculate the credit card balance 
# after one year if a person only pays the minimum monthly payment 
# required by the credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance. 
# At the end of 12 months, print out the remaining balance. 
# Be sure to print out no more than two decimal digits of accuracy - so print
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135 
# So your program only prints out one thing: 
# the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


balance = 42
monthly_payment_rate = 0.04
annual_interest_rate = 0.2

def calculate_monthly_interest_rate(_annual_interest_rate):
    return _annual_interest_rate / 12

def calculate_minimum_monthly_payment(_monthly_payment_rate, _balance):
    return _monthly_payment_rate * _balance

def calculate_monthly_unpaid_balance(_balance, _minimum_monthly_payment):
    return _balance - _minimum_monthly_payment

def get_updated_monthly_balance(_monthly_unpaid_balance, _annual_interest_rate):
    return _monthly_unpaid_balance + calculate_monthly_interest_rate(_annual_interest_rate) * _monthly_unpaid_balance

month = 0
while month < 12:
    month += 1
    minimum_monthly_payment = calculate_minimum_monthly_payment(monthly_payment_rate, balance)
    #print(f"Payment for month {month} value {minimum_monthly_payment}")
    monthly_unpaid_balance = calculate_monthly_unpaid_balance(balance, minimum_monthly_payment)
    balance = get_updated_monthly_balance(monthly_unpaid_balance, annual_interest_rate)
    
print("Remaining balance:", round(balance, 2))








    











