# Write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, 
# we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.
# The program should print out one line: 
# the lowest monthly payment that will pay off all debt in under 1 year

months = 1
balance = 3329
start = 10
temporary = start
balance = temporary
annual_interest_rate = 0.2


def updated_balance_each_month():
    """ calculate updated balance for each month """
    return monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

def monthly_interest_rate():
    """ calculate monthly enterest rate """
    return annual_interest_rate / 12.0

def monthly_unpaid_balance():
    """ calculate unpaid balance for each month """
    return previous_balance - minimum_fixed_monthly_payment

while months < 12:
    monthly_interest_rate()
    monthly_unpaid_balance()
    updated_balance_each_month()
    if start != balance:
        months += 1
        start *= 10
    else:
        break

lowest = updated_balance_each_month()

print("Lowest payment: ", round(lowest) )