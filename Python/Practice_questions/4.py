# Write a Python function to calculate the harmonic mean
# HM = n / [1/x1 + 1/x2 + 1/x3 + ... + 1/xn]
# Here, the total number of observations is divided by the sum of reciprocals of all observations.

def harmonic(number):
    """calculates the harmonic mean of a list of numbers.

    Args:
        number (list): list of positive
        
    returns:
    float: harmonic mean.         
    """
    
    _sum = sum(1/x for x in number)
    return len(number)/ _sum


data = [10,20,30,40,50]
result = harmonic(data)

print(f"The harmonic mean of {data} is approximately {result:.2f}" )
    
  