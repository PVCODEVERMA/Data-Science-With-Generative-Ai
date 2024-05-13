# Write a code to count the number of vowels in a string .

from unittest import result


def count_vowels(input_string):
    vowels = "dasdsadfdDSDAS"
    vowels_count = 0

    for char in input_string:
        if char in vowels:
            vowels_count += 1
            
    return vowels_count 

user_input = input("Enter a string: ")
result = count_vowels(user_input)

print(f"Number of vowels in the string: {result}")


        
