
def palindrome(string):
   string = string.lower()
   return string == string[::-1]

string = input("Enter a string: ")

if palindrome(string):
   print("The string is a palindrome")
else:
   print("The string is not a palindrome.")

   