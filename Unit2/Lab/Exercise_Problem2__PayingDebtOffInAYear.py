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
    """ calculate monthly interest rate """
    return _annual_interest_rate / 12.0
            
# def calculate_unpaid_balance(_balance, _monthly_payment):
#     """ calculate unpaid balance each month """
#     return (_balance) - (_monthly_payment)

# def calculate_updated_balance_each_month(_monthly_unpaid_balance, _monthly_rate):
#     """ calculate updated balance each month """
#     return (_monthly_unpaid_balance) + (_monthly_rate * _monthly_unpaid_balance)

def calculate_minimum_fixed_monthly_payment(_monthly_payment, _annual_interest_rate):
    """ calculate a minimum fixed payment that shoud be paid each month  """
    monthly_payment1 = (_monthly_payment) * (calculate_monthly_interest_rate(_annual_interest_rate)) + (_monthly_payment) * 12.0
    while monthly_payment1 <= balance:
        monthly_payment1 = (_monthly_payment) * (calculate_monthly_interest_rate(_annual_interest_rate)) + (_monthly_payment) * 12.0
        _monthly_payment += 10
    return _monthly_payment

fixed_payment = calculate_minimum_fixed_monthly_payment(monthly_payment, annual_interest_rate)

# month = 1
# while month <= 12:
#     #fixed_payment = calculate_minimum_fixed_monthly_payment(monthly_payment, annual_interest_rate)
#     unpaid_balance = calculate_unpaid_balance(balance, monthly_payment)
#     #print(f"Payment for month {month} = {unpaid_balance}")
#     updated_balance = calculate_updated_balance_each_month(unpaid_balance, annual_interest_rate / 12.0)
#     #print(f"payment for month {month} = {updated_balance}")
#     month += 1
#     balance = unpaid_balance    
    
print("Lowest payment: ", round(fixed_payment))



