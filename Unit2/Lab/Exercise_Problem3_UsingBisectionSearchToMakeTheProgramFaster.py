# how can we calculate a more accurate fixed monthly payment 
# than we did in Problem 2 without running into the problem of slow code? 
# We can make this program run faster using a technique introduced in lecture - bisection search!

# we are searching for the smallest monthly payment 
# such that we can pay off the entire balance within a year. 
# What is a reasonable lower bound for this payment value? 
# $0 is the obvious answer, but you can do better than that. 
# If there was no interest, 
# the debt can be paid off by monthly payments of one-twelfth of the original balance, 
# so we must pay at least this much every month. 
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, 
# we paid off the entire balance at the end of the year. 
# What we ultimately pay must be greater than what we would've paid in monthly installments, 
# because the interest was compounded on the balance we didn't pay off each month. 
# So a good upper bound for the monthly payment would be one-twelfth of the balance, 
# after having its interest compounded monthly for an entire year.

# Write a program that uses these bounds 
# and bisection search to find the smallest monthly payment to the cent 
# (no more multiples of $10) such that we can pay off the debt within a year. 
# Try it out with large inputs, 
# and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
# Produce the same return value as you did in Problem2

balance = 320000
annual_interest_rate = 0.2

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

def monthly_payment_lower_bound(_balance):
    return _balance / 12

def monthly_payment_upper_bound(_balance, _monthly_interest_rate):
    return (_balance * (1 + _monthly_interest_rate) ** 12) / (12.0)

def smallest_monthly_payment(_monthly_payment_lower_bound, _monthly_payment_upper_bound):
    if _monthly_payment_lower_bound == 12:
        return 12
    else:
        return _monthly_payment_upper_bound

smallest_payment = smallest_monthly_payment(_monthly_payment_lower_bound, _monthly_payment_upper_bound)
print(smallest_payment)