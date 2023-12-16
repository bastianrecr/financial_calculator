def compound_account(principal, annual_rate, compounding_periods, years): # Use this function to know the Account value after a certain amount of years of compounding each 'n' times.
    annual_rate_percentage = annual_rate / 100
    account_value = principal * ((1 + (annual_rate_percentage / compounding_periods)) ** (compounding_periods * years))
    return account_value
