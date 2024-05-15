# Default arguments: (the function calculate returns the multiplication of 4 arguments a, b ,c and d. Variable c and d will have default arguments of 45 and 10)


def calculate(a,b,c=45,d=10):
    """Returns the product of four arguments: a,b,c and d.

    Args:
        a (float or int): Fist argument.
        b (float or int): second argument.
        c (int, optional): _description_. Defaults to 45.
        d (int, optional): _description_. Defaults to 10.
    Returns:
       float or int: Product of a,b,c, and d.
    """
    return a* b *c *d

result = calculate(2,3)
print(result)
    
    