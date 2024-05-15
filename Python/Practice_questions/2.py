# Write a Python function string is palindrome or not?

def is_palindrome(string):
    """
    cheek if a string is a palindrome.
    Args:
    string: The string to cheek.
    Returns:
    True if the string is a palindrome False , otherwise.
    
    """
    string = string.lower()
    return string == string[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
