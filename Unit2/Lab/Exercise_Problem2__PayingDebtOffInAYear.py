# Write a program that calculates the minimum fixed monthly payment needed monthly_payment
# in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, 
# we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.
# The program should print out one line: 
# the lowest monthly payment that will pay off all debt in under 1 year

balance = 3926
annual_interest_rate = 0.2
monthly_payment = 10

def calculate_monthly_interest_rate(_annual_interest_rate):
    return _annual_interest_rate / 12

def calculate_monthly_unpaid_balance(_balance, _minimum_monthly_payment):
    return _balance - _minimum_monthly_payment

def get_updated_monthly_balance(_monthly_unpaid_balance, _annual_interest_rate):
    return _monthly_unpaid_balance + calculate_monthly_interest_rate(_annual_interest_rate) * _monthly_unpaid_balance

def get_remaining_balance_amount(_monthly_payment, _balance, _annual_interest_rate):
    month = 0
    while month < 12:
        month += 1
        monthly_unpaid_balance = calculate_monthly_unpaid_balance(_balance, _monthly_payment)
        _balance = get_updated_monthly_balance(monthly_unpaid_balance, _annual_interest_rate)

    return _balance

while get_remaining_balance_amount(monthly_payment, balance, annual_interest_rate, 12) > 0:
    monthly_payment += 10

print("Monthly payment: ", monthly_payment)



