# Keyword arguments:(The function simple_interest(p, t, r) is called with the keyword arguments)
# P = (100 × S.I.)/(R × T)


def calculate(a,b,c):
    """
    calculates the principal amount using the simple interest formula.

    Args:
        a (float): The rate of interest amount.
        b (float): The rate of interest (as a percentage).
        c (float): The time duration (in years).
    Returns:
    float: Principal amount.
    """
    
    rate_decimal = b / 100
    
    principal = (100 * a)/ (a *c)
    return principal
si_amount = 500
interest_rate = 5
time_period =2

principal_amount = calculate(si_amount,interest_rate,time_period)
print(principal_amount)