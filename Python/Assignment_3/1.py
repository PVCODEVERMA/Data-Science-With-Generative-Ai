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


# 11. write a code to remove all occurrences of  a specific element from a list.

# def remove_occurrences(lst,element):
#     return [item for item in lst if item != element]
    
# # Example using    
# my_list = [1,2,3,4,2,5,2,6]
# element_to_remove = 2
# updated_list = remove_occurrences(my_list,element_to_remove)
# print(updated_list)

#12. Implement a code to find the second largest number in a given list of integers.

# list = [55,1,45,68,159,75,5,159]

# def find_second_maximum(list1):
#     first_max = max(list[0],list1[1])
#     second_max = min(list1[0],list1[1])
    
#     for i in range(2, len(list1)):
#         if list1[i] > first_max:
#             second_max = first_max
#             first_max = list1[i]
        
#         elif list1[i] > second_max and first_max != list1[i]:
#             second_max = list1[i]
#     return second_max

# print("second maximum number is ", find_second_maximum(list))
    
    
#13. create a code to count the occurrence of each element in a list and return a dictionary with elements as keys and their counts as values.

# def count_occurrences(lst):
#     count_dist = {}
#     for item in lst:
#         if item in count_dist: 
#             count_dist[item] += 1
#         else:
#             count_dist[item] = 1
#     return count_dist

# my_list = [1,2,2,3,4,4,4,5,5]
# occurrence_dist = count_occurrences(my_list)
# print(occurrence_dist)

#write a code to reverse a list in place without using any built-in reverse functions.


# def reverse_list(lst):
#     left = 0
#     right = len(lst) - 1
    
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
        
#         left += 1
#         right -= 1

# my_list = [1,2,3,4,5]
# reverse_list(my_list)
# print(my_list)
        

#15. implement a code to find and remove duplicates from a list while preserving the original order of elements.

# def remove_duplicates(lst):
#     seen = set()
#     result = []
    
#     for item in lst:
#         if item not in seen:
#             result.append(item)
#             seen.add(item)
            
#     return result



# my_list = [1,2,2,3,4,4,5,1,6]
# unique_list = remove_duplicates(my_list)

# print(unique_list)

#16. create a code to check if a give list is sorted (either in ascending order) or not.

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        return True 

my_list = [1,2,3,4,5]
print(is_sorted(my_list))

my_list2 = [5,3,2,4]
print(is_sorted(my_list2))

#17. write a code to merge two sorted lists into a single list
