#1. Write a code to reverse a string ?

# x = "HELLO"[::-1]
# print(x);  #OLLEH

#2. write a code to count the number of vowels in a string.

# string = input("Enter string: ")
# vowels = 0
# for i in string:
#     if(i=='a' or i=='i' or i=='o' or i=='u' or i=='A' or i=='I' or i=='O' or i=='U'):
#         vowels=vowels+1
# print("Number of vowels are:", vowels)

# 3. write a code to check if a given string is a palindrome or not

# a  = input("Enter string:")
# b = a[-1::-1]

# if(a==b):
#     print("Palindrome string")
# else:
#     print("not Palindrome string")


# 4. Write a code to check if two given strings are anagrams of each other.  

# word1 = input("Enter word1:\n")
# word2 = input("Enter word2:\n")


# if(sorted(word1) == sorted(word2)):
#     print("Anagrams")
# else:
#     print("Not anagrams")

# 5. write a code to find all occurrence of a given substring within another string. 


# my_string = input("Enter a string :\n")
# my_substring = input("Enter a Substring :\n")

# my_count = my_string.count(my_substring)

# print("substring occurs %d times " % my_count)


# 6. write a code to perform basic string compression using the counts of repeated characters.    

# def compress_string(s):
#     # If the string is empty, return it as is
#     if not s:
#         return s

#     compressed = []
#     count = 1

#     # Iterate through the string
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             # Append the character and its count
#             compressed.append(s[i - 1] + str(count))
#             count = 1

#     # Append the last character and its count
#     compressed.append(s[-1] + str(count))

#     # Convert the list back to a string
#     compressed_string = ''.join(compressed)

#     # Return the compressed string only if it's shorter, otherwise return the original string
#     return compressed_string if len(compressed_string) < len(s) else s


# # Example usage
# input_string = "aabcccccaaa"
# compressed_output = compress_string(input_string)
# print(compressed_output)


# 7. Write a code to determine if a string has all unique characters.  
# def check_unique_chars(string):
#     if string is None:
#         return False
#     for char in string:
#         if string.count(char) > 1:
#             return False
#     return True  # This should be outside the loop
# user_input = input("Enter a string: ")
# result = check_unique_chars(user_input)
# print(f"Does the string have all unique characters? {result}")


# 8. Write a code to convert a  given string to uppercase or lowercase. 

# string = input("Enter a string:\n")

# print(string.lower())
# print(string.upper())


# 9. write a code to count the number of words in a string.  

# string = len(input("Enter a string: ").split())
# print(string)
# OR
# string = input("enter a string: \n")
# str_list = string.split()

# print(len(str_list))


# 9. write a code to concatenate two string without using the + operator.  


# def concatenate_strings(str1,str2):
#     result = ''.join([*str1,*str2])
#     return result

# string1  = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# result = concatenate_strings(string1, string2)

# print(f"concatenated string: {result}")


# 11. write a code to 