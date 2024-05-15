# Write a Python function check the number is prime or not?

def is_prime(n):
    """
    cheek if a number is prime.
    
    Args:
    n:The number to cheek.
    Returns:
    True if n is prime false otherwise.
    """
    
    if n<2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n% i == 0:
            return False
        
        return True
