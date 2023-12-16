def financial_calculator():
    print('Welcome to the financial calculator!')
    principal = get_principal()
    rate = get_rate(principal)
    compounding = get_compounding()
    years = get_years()
    result = compound_account(principal, rate, compounding, years)
    formatted_result = "{:,.2f}".format(result)
    print("After {time} years, your investment of ${principal} at a {rate}% annual interest rate, compounded {compounding} times per year, will be worth ${account}.".format(time=years, account=formatted_result, principal=principal, rate=rate, compounding=compounding))

def error_message():
    print('Sorry, this input is not valid. Please make sure your input meets the requirements mentioned in the instructions.')

def get_principal():
    principal = input('What amount of money would you like to invest? \n> ')
    if principal.isdigit():
        return float(principal)
    else:
        error_message()
        return get_principal()

def get_rate(principal):
    rate = float(input('What would be the annual rate at which you would invest those ${amount}? (Please enter the rate as an integer, not as a decimal) \n> '.format(amount=principal)))
    return rate

def get_compounding():
    answer = input('How often will interest be compounded? \n[a] Daily compounding \n[b] Monthly compounding \n[c] Quarterly Compounding \n[d] Semi-Annual Compounding \n[e] Annual Compounding \n> ')
    daily_compounding = 365 # Days in a year
    monthly_compounding = 12 # Months in a year
    quarterly_compounding = 4 # Quarters in a year
    semi_annual_compounding = 2 # Twice per year
    annual_compounding = 1 # Once per year

    if answer.lower() == 'a':
        return daily_compounding
    elif answer.lower() == 'b':
        return monthly_compounding
    elif answer.lower() == 'c':
        return quarterly_compounding
    elif answer.lower() == 'd':
        return semi_annual_compounding
    elif answer.lower() == 'e':
        return annual_compounding
    else:
        error_message()
        return get_compounding()

def get_years():
    years = int(input('How many years will you keep this investment for? (Please enter an amount greater than or equal to zero)\n> '))
    if years >= 0:
        return years
    else:
        error_message()
        return get_years()

def compound_account(principal, annual_rate, compounding_periods, years): # Use this function to know the Account value after a certain amount of years of compounding each 'n' times.
    annual_rate_percentage = annual_rate / 100
    account_value = principal * ((1 + (annual_rate_percentage / compounding_periods)) ** (compounding_periods * years))
    return account_value

financial_calculator()